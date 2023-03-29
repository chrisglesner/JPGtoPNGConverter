'''

This script simply converts .JPG (or any other image extension) to a .PNG.

Your current and new directories are defined in the sys.argv[1] and [2] indices. 

These are done when you run the script from your terminal session.

'''

import sys
import os
import glob
from PIL import Image

directory = os.listdir(sys.argv[1])
new_path = sys.argv[2]

if not os.path.exists(new_path):
    os.makedirs(new_path)

for file in directory:
    old_image = Image.open(f'{sys.argv[1]}{file}')
    file_without_ext = os.path.splitext(file)[0]
    new_image = old_image.save(f'{new_path}/{file_without_ext}.png')