#!/usr/bin/env python3
"""Render final-size and greyscale previews; BSD-3-Clause, Antonio Clim."""
import argparse
from pathlib import Path
import fitz
from PIL import Image

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--kit-root', type=Path, default=Path(__file__).resolve().parents[1])
args = parser.parse_args()
root = args.kit_root.resolve()
out = root/'verification/previews'
out.mkdir(parents=True, exist_ok=True)
for i in range(1,4):
    for kind, source in [('reference', root/f'reference_exports/Fig{i}.pdf'),
                         ('native', root/f'native_exports/Fig{i}_Editable.pdf')]:
        document = fitz.open(source)
        pixmap = document[0].get_pixmap(matrix=fitz.Matrix(150/72,150/72))
        image = Image.frombytes('RGB', [pixmap.width, pixmap.height], pixmap.samples)
        image.save(out/f'Fig{i}_{kind}_150dpi.png', dpi=(150,150))
        image.convert('L').save(out/f'Fig{i}_{kind}_grayscale_150dpi.png', dpi=(150,150))
print('Rendered 12 final-size previews (5 × 6 in at 150 dpi).')
