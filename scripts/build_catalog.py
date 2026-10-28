#!/usr/bin/env python3
"""Build a contact sheet of source-art PNGs in the content pack. Requires Pillow."""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
files=sorted((ROOT/'assets/source_tiles').rglob('*.png'))
cols=8; cell_w=128; cell_h=128; thumb=88; rows=(len(files)+cols-1)//cols
out=Image.new('RGB',(cols*cell_w,rows*cell_h),(238,238,238))
d=ImageDraw.Draw(out)
try: font=ImageFont.truetype('DejaVuSans.ttf',10)
except: font=ImageFont.load_default()
for i,p in enumerate(files):
    im=Image.open(p).convert('RGBA'); im.thumbnail((thumb,thumb),Image.Resampling.NEAREST)
    x=(i%cols)*cell_w+(cell_w-im.width)//2; y=(i//cols)*cell_h+3
    checker=Image.new('RGBA',(thumb,thumb),(255,255,255,255)); checker.alpha_composite(im,((thumb-im.width)//2,(thumb-im.height)//2))
    out.paste(checker.convert('RGB'),((i%cols)*cell_w+(cell_w-thumb)//2,y))
    d.text(((i%cols)*cell_w+4,(i//cols)*cell_h+94),p.stem[:23],fill=(20,20,20),font=font)
    d.text(((i%cols)*cell_w+4,(i//cols)*cell_h+108),p.parent.name[:20],fill=(65,65,65),font=font)
out.save(ROOT/'previews/tile_catalog.png',optimize=True)
print(f'Catálogo criado: {len(files)} imagens -> previews/tile_catalog.png')
