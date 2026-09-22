# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Render assets/figures/src/*.html to assets/figures/*.png with headless Chrome.

Usage:
  uv run tools/figures.py            # all figures
  uv run tools/figures.py 04-1 08-2  # only these
"""

import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "figures" / "src"
OUT = ROOT / "assets" / "figures"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SCALE = 2
PAD = 36 * SCALE


def render(html: Path) -> Path:
    with tempfile.TemporaryDirectory() as tmp:
        shot = Path(tmp) / "shot.png"
        subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--virtual-time-budget=6000",
                        f"--force-device-scale-factor={SCALE}", "--window-size=800,2600",
                        f"--screenshot={shot}", html.as_uri()], check=True, capture_output=True)
        img = Image.open(shot).convert("RGB")
    bg = img.getpixel((2, img.height - 2))
    px = img.load()
    bottom = img.height - 1
    while bottom > 0 and all(px[x, bottom] == bg for x in range(0, img.width, 3)):
        bottom -= 1
    img = img.crop((0, 0, img.width, min(img.height, bottom + PAD)))
    out = OUT / f"{html.stem}.png"
    img.quantize(colors=256, method=Image.Quantize.MEDIANCUT).save(out, optimize=True)
    return out


def main():
    names = sys.argv[1:]
    files = sorted(p for p in SRC.glob("*.html") if not names or p.stem in names)
    for html in files:
        out = render(html)
        w, h = Image.open(out).size
        print(f"{out.relative_to(ROOT)}  {w}x{h}  {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
