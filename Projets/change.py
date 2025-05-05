
import os
import re

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # # Remove full <div class="right-column"> ... </div> blocks
    # content = re.sub(r'<div class="right-column">.*?</div>', '', content, flags=re.DOTALL)

    # Add p1, p2, ... classes to each image with class="photo"
    def add_class(match):
        i = add_class.counter
        add_class.counter += 1
        return match.group(0).replace('class="photo', f'class="photo p{i}')

    add_class.counter = 1
    content = re.sub(r'<img[^>]*class="photo[^"]*"[^>]*>', add_class, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Apply to all .html files in current folder
for filename in os.listdir("."):
    if filename.endswith(".html"):
        process_file(filename)
