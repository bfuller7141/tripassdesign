import os
import re

# Define the incorrect and corrected favicon lines
incorrect_favicon_line = r"<link rel='shortcut icon' type='image/x-icon' href='theme\\assets\\images\\image_2024-06-24_105300454.ico' />"
corrected_favicon_line = "<link rel='shortcut icon' type='image/x-icon' href='/assets/images/image_2024-06-24_105300454.ico' />"

# Define the base directory
base_dir = r'C:\Users\Tripass - Brandon\Documents\GitHub\tripassdesign\theme'

# Function to update the favicon line in a given file
def update_favicon_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    updated_html_content = re.sub(incorrect_favicon_line, corrected_favicon_line, html_content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_html_content)

    print(f"Updated favicon in {file_path}")

# Traverse the directories and update HTML files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            update_favicon_in_file(file_path)

print("Favicon lines updated successfully in all specified folders.")
