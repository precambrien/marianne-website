import os
from PIL import Image

# CONFIG
input_folder = "./projets_images/"
output_folder = "./projets_images_small/"
max_width = 1600
max_height = 1600

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Walk through all subfolders
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, input_folder)
            output_dir = os.path.join(output_folder, relative_path)
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, file)

            # Open and resize
            with Image.open(input_path) as img:
                img.thumbnail((max_width, max_height))
                img.save(output_path, optimize=True, quality=85)

print("✅ All images resized successfully!")
