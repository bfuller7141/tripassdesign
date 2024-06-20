import os
from bs4 import BeautifulSoup
import cssutils
import jsbeautifier

# Base directory containing all your folders
base_directory = r'C:\Users\Tripass - Brandon\Documents\GitHub\tripassdesign\theme'

# Function to clean and enhance HTML
def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Add lang attribute if missing
    if not soup.html.has_attr('lang'):
        soup.html['lang'] = 'en'

    return soup.prettify()

# Function to clean CSS
def clean_css(css_content):
    parser = cssutils.CSSParser()
    sheet = parser.parseString(css_content)
    return sheet.cssText.decode('utf-8')

# Function to clean JavaScript
def clean_js(js_content):
    opts = jsbeautifier.default_options()
    opts.indent_size = 2
    return jsbeautifier.beautify(js_content, opts)

# List of directories to clean
directories_to_clean = [
    base_directory,
    os.path.join(base_directory, 'contact'),
    os.path.join(base_directory, 'legal'),
    os.path.join(base_directory, 'assets', 'css'),
    os.path.join(base_directory, 'assets', 'js')
]

# Iterate over the specified directories and clean files
for directory in directories_to_clean:
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            cleaned_content = content

            if file.endswith('.html'):
                cleaned_content = clean_html(content)
            elif file.endswith('.css'):
                cleaned_content = clean_css(content)
            elif file.endswith('.js'):
                cleaned_content = clean_js(content)

            if cleaned_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                print(f"Cleaned and updated: {file_path}")
            else:
                print(f"No changes made to: {file_path}")

print("Code cleaning completed.")