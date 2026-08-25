from pathlib import Path 
from PIL import Image, ImageFilter

script_directory = Path(__file__).resolve().parent
image_path = script_directory / "Pokedex" /"pikachu.jpg"

img = Image.open(image_path)
filtered_img = img.convert('L')
box  = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png","png")