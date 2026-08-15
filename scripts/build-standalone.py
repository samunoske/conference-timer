#!/usr/bin/env python3
"""Build a single all-in-one HTML file from the split sources.

Usage:  python3 scripts/build-standalone.py
Output: standalone/conference-timer.html
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "standalone" / "conference-timer.html"

html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "styles.css").read_text(encoding="utf-8")
js = (ROOT / "app.js").read_text(encoding="utf-8")

html = html.replace(
    '<link rel="stylesheet" href="styles.css">',
    "<style>\n" + css + "\n</style>",
)
html = html.replace(
    '<script src="app.js"></script>',
    "<script>\n" + js + "\n</script>",
)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes)")
