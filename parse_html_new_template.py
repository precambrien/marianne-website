
from bs4 import BeautifulSoup
import os

# Folders
old_folder = "Projets_old"
new_folder = "Projets"
template_path = "template.html"

# Load the template.html once
with open(template_path, "r", encoding="utf-8") as template_file:
    new_template = template_file.read()

# Make sure output folder exists
os.makedirs(new_folder, exist_ok=True)

# Go through each old file
for filename in os.listdir(old_folder):
    if filename.endswith(".html"):
        filepath = os.path.join(old_folder, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        
        # Extract <title>
        page_title = soup.title.string.strip() if soup.title else "No Title"
        
        # Inside .body-container
        container = soup.find(class_="bodyContainer")
        if not container:
            print(f"⚠️ No .bodyContainer found in {filename}")
            continue
        
        # Extract pure text content by class name
        main_title_elem = container.find(class_="title")
        undertitle_elem = container.find(class_="undertitle")
        text_blocks = container.find_all(class_="text")
        
        main_title = main_title_elem.get_text(strip=True) if main_title_elem else ""
        undertitle = undertitle_elem.get_text(strip=True) if undertitle_elem else ""
        text_content = "\n".join(text.get_text(strip=True) for text in text_blocks)
        
        # Prepare images as HTML (full <img> tags)
        images = container.find_all("img")
        images_html = "\n".join(str(img) for img in images)
        
        # Fill template
        new_html = new_template.format(
            page_title=page_title,
            main_title=main_title,
            undertitle=undertitle,
            text_content=text_content,
            images=images_html
        )
        
        # Save new file
        output_path = os.path.join(new_folder, filename)
        with open(output_path, "w", encoding="utf-8") as new_file:
            new_file.write(new_html)
        
        print(f"✅ Converted {filename}")
