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

# Folder containing the HTML files
theme_folder = 'theme'

# Specific script content to be removed
script_content_to_remove = '''<script src="/assets/js/udesly-11ty.min.js" async="" defer=""></script>{{ settings.site.footer_additional_content }}<script>window.netlifyIdentity&&window.netlifyIdentity.on("init",a=>{a||window.netlifyIdentity.on("login",()=>{document.location.href="/admin/"})});</script><script type="module">import*as UdeslyBanner from"https://cdn.jsdelivr.net/npm/udesly-ad-banner@0.0.4/loader/index.js";UdeslyBanner.defineCustomElements(),document.body.append(document.createElement("udesly-banner"));</script>'''

# Function to replace placeholders and remove specific script content in an HTML file
def replace_placeholders_in_file(file_path, links, texts, images, script_content_to_remove):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove the specific script content
    content = content.replace(script_content_to_remove, '')

    # Replace placeholders
    for key, value in {**links, **texts, **images}.items():
        placeholder = f'{{{{ {key} }}}}'
        if placeholder in content:
            print(f'Replacing placeholder: {placeholder} with value: {value} in file: {file_path}')
        content = content.replace(placeholder, value)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Traverse all files in the theme folder and its subfolders
for root, dirs, files in os.walk(theme_folder):
    for filename in files:
        if filename.endswith('.html'):
            file_path = os.path.join(root, filename)
            print(f'Processing file: {file_path}')
            replace_placeholders_in_file(file_path, links, texts, images, script_content_to_remove)

print("Placeholders replaced and script content removed successfully.")
