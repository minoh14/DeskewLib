import os
from PIL import Image  #pip install pillow

def merge_images_to_pdf(folder, merged):
    files = sorted(os.listdir(folder))
    if len(files) > 0:
        pages = []
        for file in files:
            img = Image.open(os.path.join(folder, file))
            pages.append(img.convert("RGB"))
        pages[0].save(merged, save_all=True, append_images=pages[1:])
