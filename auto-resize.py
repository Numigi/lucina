from PIL import Image
import os
import re

# Configuration
src_dir = "src"
dist_dir = "./dist/numigi"
resolutions = [135, 512, 1024]

# Create the destination folder if it does not exist
os.makedirs(dist_dir, exist_ok=True)

# Extract information from the filename
def extract_info(filename):
    match = re.match(r'numigien=([^,]+), style=([^\.]+)\.png', filename)
    if match:
        return match.groups()
    return None, None

# Resize and save images
def resize_and_save(image_path, person, style, resolution):
    # Path to the style folder
    style_path = os.path.join(dist_dir, style)
    os.makedirs(style_path, exist_ok=True)
    
    # Path to the resolution folder
    res_path = os.path.join(style_path, f"{resolution}px")
    os.makedirs(res_path, exist_ok=True)
    
    # Resize and save
    with Image.open(image_path) as img:
        img = img.resize((resolution, resolution), Image.Resampling.LANCZOS)
        # File renamed to only include the numigien name
        save_path = os.path.join(res_path, f"{person}.png")
        img.save(save_path, "PNG")

# Browse files in the source folder
for filename in os.listdir(src_dir):
    if filename.endswith(".png"):
        person, style = extract_info(filename)
        if person and style:
            image_path = os.path.join(src_dir, filename)
            for resolution in resolutions:
                resize_and_save(image_path, person, style, resolution)

print("Autoresizing done.")
