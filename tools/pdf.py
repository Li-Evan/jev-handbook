"""Typeset the PDF edition with WeasyPrint.

Figures behave like print floats. When one no longer fits at the bottom of a page and would
leave a big gap there, it is shrunk to fit if that costs little, otherwise moved after the
next paragraph (or before the previous one), and the book is laid out again.

Usage: python tools/pdf.py OUT.pdf PRINT.html -- PANDOC_COMMAND...
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent
MM = 96 / 25.4
GAP = 25 * MM            # a page may end this much early without anything being moved
SHRINK = 0.6             # shrink a figure to fit when it keeps at least this share of its height
TRIES = [1, 2, 3, -1, -2, -3, 4]
SKIP = {"html", "body", "main", "nav", "section"}


def flow_boxes(page):
    for box in page._page_box.descendants():
        if getattr(box, "element_tag", None) not in (None, *SKIP) and box.element is not None:
            yield box


def lead_figure(page, top):
    """The figure a page opens with, possibly under a section heading that was pulled along."""
    boxes = list(flow_boxes(page))
    if not boxes or abs(boxes[0].position_y - top) > 2:
        return None
    for box in boxes:
        if box.element_tag in ("h2", "h3"):
            continue
        return box if box.element_tag == "figure" else None


def pushed_figures(doc):
    """Figures that start a page while the page before ends with a big gap."""
    found = []
    for prev, page in zip(doc.pages, doc.pages[1:]):
        top = page._page_box.content_box_y()
        bottom = top + page._page_box.height
        first = lead_figure(page, top)
        if first is None:
            continue
        used = max((b.position_y + b.margin_height() for b in flow_boxes(prev)), default=bottom)
        gap = bottom - used
        img = next((b for b in first.descendants() if getattr(b, "element_tag", None) == "img"), None)
        if img is None or gap < GAP:
            continue
        found.append((img.element.get("src"), gap, first.margin_height(), img.height))
    return found


def main():
    out, printable, pandoc = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[sys.argv.index("--") + 1:]
    moves, shrink, tried, gave_up = {}, {}, {}, set()
    with tempfile.TemporaryDirectory() as tmp:
        floats = Path(tmp) / "floats.json"
        for rounds in range(1, 15):
            floats.write_text(json.dumps({"float_moves": moves, "float_shrink": shrink}))
            subprocess.run([*pandoc, "--metadata-file", str(floats), "--output", str(printable)], check=True, cwd=ROOT)
            doc = HTML(filename=str(printable), base_url=str(ROOT)).render()
            pushed = [p for p in pushed_figures(doc) if p[0] not in gave_up]
            if not pushed:
                break
            for src, gap, figure_height, img_height in pushed:
                room = gap - (figure_height - img_height) - 2 * MM
                if room >= SHRINK * img_height and src not in shrink:
                    shrink[src] = round(room / MM, 1)
                    moves.pop(src, None)
                elif tried.get(src, 0) < len(TRIES):
                    moves[src] = TRIES[tried.get(src, 0)]
                    tried[src] = tried.get(src, 0) + 1
                else:
                    gave_up.add(src)
        print(f"pdf: {len(doc.pages)} pages, {rounds} layout rounds, {len(moves)} figures moved, "
              f"{len(shrink)} shrunk, {len(pushed_figures(doc))} gaps left")
        doc.write_pdf(out, optimize_images=True)


if __name__ == "__main__":
    main()
