import os
import json

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, str(v)))
    return dict(items)

# Paths to the JSON files
data_folder = 'cms/_data'
links_file = os.path.join(data_folder, 'links.json')
texts_file = os.path.join(data_folder, 'texts.json')
images_file = os.path.join(data_folder, 'images.json')

# Read and flatten JSON files
with open(links_file, 'r', encoding='utf-8') as file:
    links = flatten_dict(json.load(file))

with open(texts_file, 'r', encoding='utf-8') as file:
    texts = flatten_dict(json.load(file))

with open(images_file, 'r', encoding='utf-8') as file:
    images = flatten_dict(json.load(file))

# Print the flattened data for debugging
print("Links data:", links)
print("Texts data:", texts)
print("Images data:", images)

# Folder containing the HTML files
theme_folder = 'theme'

# Replace placeholders in the HTML files
for filename in os.listdir(theme_folder):
    if filename.endswith('.html'):
        file_path = os.path.join(theme_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Initial content for debugging
        original_content = content

        # Replace placeholders
        for key, value in links.items():
            placeholder = f'{{{{ links.{key} }}}}'
            if placeholder in content:
                print(f"Replacing {placeholder} with {value}")
            content = content.replace(placeholder, value)
        
        for key, value in texts.items():
            placeholder = f'{{{{ texts.{key} }}}}'
            if placeholder in content:
                print(f"Replacing {placeholder} with {value}")
            content = content.replace(placeholder, value)
        
        for key, value in images.items():
            placeholder = f'{{{{ images.{key} }}}}'
            if placeholder in content:
                print(f"Replacing {placeholder} with {value}")
            content = content.replace(placeholder, value)

        # Check if content was changed for debugging
        if content != original_content:
            print(f"Changes made to {filename}")

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Placeholders replaced successfully.")
