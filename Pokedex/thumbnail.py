from pathlib import Path
from PIL import Image, ImageFilter

script_directory = Path(__file__).resolve().parent
image_path = script_directory / "astro.jpg"

img = Image.open(image_path)
img.thumbnail((400, 400)) # useful for social media images, it protects the Aspect Ratio
img.save('thumbnail.jpg')
print(img.size)