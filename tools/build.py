# /// script
# requires-python = ">=3.10"
# dependencies = ["weasyprint"]
# ///
"""Build the book from book/*.md: EPUB, web edition and PDF.

Usage:
  uv run tools/build.py

Needs pandoc, pango (brew install pango) and a CJK font; epubcheck is optional.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"
DIST = ROOT / "dist"
NAME = "jev-handbook"


def chapters():
    files = sorted(p for p in BOOK.glob("*.md") if p.name[:2].isdigit())
    if not files:
        sys.exit("no chapters in book/")
    return [str(p) for p in files]


def run(cmd):
    print("$", " ".join(cmd[:6]), "…" if len(cmd) > 6 else "")
    subprocess.run(cmd, check=True, cwd=ROOT)


def main():
    if not shutil.which("pandoc"):
        sys.exit("pandoc is required: brew install pandoc")
    DIST.mkdir(exist_ok=True)
    meta = str(BOOK / "metadata.yaml")
    common = ["pandoc", meta, *chapters(), "--from", "markdown+east_asian_line_breaks", "--toc", "--toc-depth=2",
              "--lua-filter", "tools/book.lua", "--css", "tools/book.css"]

    epub = DIST / f"{NAME}.epub"
    run([*common, "--to", "epub3", "--split-level=1", "--output", str(epub)])

    site = DIST / "site"
    site.mkdir(exist_ok=True)
    shutil.copy(ROOT / "tools" / "book.css", site / "book.css")
    shutil.copy(ROOT / "tools" / "web.css", site / "web.css")
    shutil.copy(ROOT / "assets" / "cover.png", site / "cover.png")
    for name in ("figures", "shots"):
        out = site / "assets" / name
        out.mkdir(parents=True, exist_ok=True)
        for image in (ROOT / "assets" / name).glob("*.*"):
            if image.suffix in (".png", ".jpg"):
                shutil.copy(image, out / image.name)
    run([*common[:-2], "--to", "html5", "--standalone", "--css", "book.css", "--css", "web.css", "--template", "tools/web.html",
         "--metadata", "pagetitle=Jev 实战手册", "--output", str(site / "index.html")])

    pdf = DIST / f"{NAME}.pdf"
    printable = DIST / "print.html"
    run([*common[:-2], "--to", "html5", "--standalone", "--toc-depth=1", "--template", "tools/print.html",
         "--css", "tools/print.css", "--metadata", "pagetitle=Jev 实战手册", "--output", str(printable)])
    env = dict(os.environ)
    if sys.platform == "darwin":
        env.setdefault("DYLD_FALLBACK_LIBRARY_PATH", "/opt/homebrew/lib")
    print("$ weasyprint", printable.name, pdf.name)
    subprocess.run([sys.executable, "-m", "weasyprint", "--base-url", str(ROOT), "--optimize-images", "--dpi", "200",
                    "--jpeg-quality", "85", str(printable), str(pdf)],
                   check=True, cwd=ROOT, env=env)

    shutil.copy(epub, site / epub.name)
    shutil.copy(pdf, site / pdf.name)
    if shutil.which("epubcheck"):
        run(["epubcheck", str(epub)])
    else:
        print("epubcheck not found; skipped validation (brew install epubcheck)")
    print("done:", ", ".join(str(p.relative_to(ROOT)) for p in sorted(DIST.glob("*.*"))))


if __name__ == "__main__":
    main()
