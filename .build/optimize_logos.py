"""Optimize source PNGs: resize to max 120x120, quantize to 256-color palette.
Outputs base64 strings ready to embed in SVGs."""
import base64, io, pathlib
from PIL import Image

SOURCES = {
    "python":  r"D:\Imagenes\python-removebg-preview.png",
    "houdini": r"D:\Imagenes\Proyecto nuevo.png",
    "pyside":  r"D:\Imagenes\pysideLogo-removebg-preview.png",
}

OUT = pathlib.Path(r"D:\Dev\github_personal\Raul-Olivares-TD\.build\logos")
OUT.mkdir(parents=True, exist_ok=True)

for name, src in SOURCES.items():
    img = Image.open(src).convert("RGBA")
    # square pad to preserve aspect ratio
    side = max(img.size)
    canvas = Image.new("RGBA", (side, side), (255, 255, 255, 0))
    canvas.paste(img, ((side - img.size[0]) // 2, (side - img.size[1]) // 2), img)
    canvas = canvas.resize((120, 120), Image.Resampling.LANCZOS)
    # quantize palette to drop size while keeping alpha
    quant = canvas.quantize(colors=64, method=Image.Quantize.FASTOCTREE)
    buf = io.BytesIO()
    quant.save(buf, format="PNG", optimize=True)
    data = buf.getvalue()
    out_png = OUT / f"{name}.png"
    out_png.write_bytes(data)
    out_b64 = OUT / f"{name}.b64.txt"
    out_b64.write_text(base64.b64encode(data).decode())
    print(f"{name:8s} {src.split(chr(92))[-1]:40s} {len(data):6d} bytes  ({out_png.name})")