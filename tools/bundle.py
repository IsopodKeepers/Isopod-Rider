#!/usr/bin/env python3
"""Pack isopod-rider.html + assets/ + music/ into ONE self-contained HTML file.

Usage:  python3 tools/bundle.py            -> writes isopod-rider-bundled.html
"""
import base64, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
MIME = {'.png': 'image/png', '.jpg': 'image/jpeg', '.mp3': 'audio/mpeg', '.wav': 'audio/wav'}

src = (ROOT / 'isopod-rider.html').read_text()

def inline(m):
    q, path = m.group(1), m.group(2)
    data = base64.b64encode((ROOT / path).read_bytes()).decode()
    return f"{q}data:{MIME[pathlib.Path(path).suffix]};base64,{data}{q}"

out = re.sub(r"(['\"])((?:assets|music)/[\w.-]+\.(?:png|jpg|mp3|wav))\1", inline, src)
dest = ROOT / 'isopod-rider-bundled.html'
dest.write_text(out)
print(f"wrote {dest.name} ({dest.stat().st_size/1e6:.1f} MB)")
