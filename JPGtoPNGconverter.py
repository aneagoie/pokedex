import sys
import os
from PIL import Image, ImageFilter

# path = sys.argv[0]
# directory = sys.argv[1]

# if not os.path.exists(directory):
#     os.makedirs(directory)

# for filename in os.listdir(path):
# clean_name = os.path.splitext(filename)[0]
# img = Image.open(f'{path}pikachu.jpg')
# #added the / in case user doesn't enter it. You may want to check for this and add or remover it.
# img.save(f'{directory}/{clean_name}_test.png', 'png')
# print('all done!')

img = Image.open('./astro.jpg')
new_img = img.resize((400,400))
new_img.save('thumb.jpg')