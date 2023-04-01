import os
from PIL import Image  #pip install pillow
import tifftools       #pip install tifftools

def get_tif_pages(file):
    img = Image.open(file)
    return img.n_frames

def split_tif_pages(file, folder):
    basename = os.path.basename(file)
    filename, ext = os.path.splitext(basename)
    img = Image.open(file)
    for i in range(img.n_frames):
        img.seek(i)
        img.save(os.path.join(folder, f"{filename}_{i:04}{ext}"))

def merge_tif_files(folder, merged):
    files = sorted(os.listdir(folder))
    if len(files) > 0:
        pages = []
        for file in files:
            pages.append(os.path.join(folder, file))
        tifftools.tiff_concat(pages, merged, overwrite=True)
