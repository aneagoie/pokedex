import os
from PIL import Image

folder_name, new_folder_name = input().split()
way = os.path.abspath(new_folder_name)
if not os.path.isdir(way) :
    os.makedirs(new_folder_name)

with os.scandir(folder_name) as files :
    for each in files :
        img = Image.open(f'{folder_name}/{each.name}')
        new_file_name = each.name.replace('jpg', 'png')
        img.save(f'{new_folder_name}/{new_file_name}')


