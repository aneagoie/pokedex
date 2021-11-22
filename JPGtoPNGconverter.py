import sys
import os
from PIL import Image

image_folder = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)
    

for filename in os.listdir(image_folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{image_folder}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remove it.
    if '/' in directory:
        corrected_path = directory.replace('/', '')
        img.save(f'{corrected_path}/{clean_name}.png', 'png')
    else:
        img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')
