import json
import os

# Function to read JSON data
def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to perform replacements
def replace_placeholders(html_content, replacements):
    for key, value in replacements.items():
        html_content = html_content.replace(f"{{{{ {key} }}}}", value)
    return html_content

# Main function
def main():
    # Paths to the JSON files
    links_json_path = 'cms/_data/links.json'
    texts_json_path = 'cms/_data/texts.json'
    images_json_path = 'cms/_data/images.json'
    
    # Read JSON data
    links_data = read_json(links_json_path)
    texts_data = read_json(texts_json_path)
    images_data = read_json(images_json_path)

    # Combine all replacements into one dictionary
    all_replacements = {**links_data, **texts_data, **images_data}

    # Get all HTML files in the theme directory
    theme_dir = 'theme'
    html_files = [os.path.join(theme_dir, file) for file in os.listdir(theme_dir) if file.endswith('.html')]

    # Process each HTML file
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Perform replacements
        modified_html_content = replace_placeholders(html_content, all_replacements)

        # Save the modified HTML to a new file in the same directory with a prefix `output_`
        output_file = os.path.join(theme_dir, f'output_{os.path.basename(html_file)}')
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(modified_html_content)

        print(f'Replacements completed for {html_file}, saved as {output_file}')

if __name__ == '__main__':
    main()
