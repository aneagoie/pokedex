import sys 
import os 
from PIL import Image 


# grab first and second argument 

if len(sys.argv) < 3:
    print(f"Usage: python {sys.argv[0]} <image_folder> <output_folder>")
    sys.exit(1)

image_folder = sys.argv[1] #Pokedex folder
output_folder = sys.argv[2] # new folder

print(image_folder, output_folder)

# check if new/ exists, if not create it 
if not os.path.exists(output_folder): 
    os.makedirs(output_folder)

# loop through pokedex
for filename in os.listdir(image_folder):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img = Image.open(os.path.join(image_folder, filename))

    new_filename = os.path.splitext(filename)[0] + ".png"
    img.save(os.path.join(output_folder, new_filename), "PNG")

    print(f"Converted {filename}")

print("All done!")

# convert images to png 
# save to the new folder 

