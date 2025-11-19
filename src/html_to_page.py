import os
import shutil

from block_markdown import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("Error No Title")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown = file.read()
    with open(template_path, 'r') as file:
        template = file.read()
    html_nodes = markdown_to_html_node(markdown)
    html = html_nodes.to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}",title).replace("{{ Content }}", html)
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(page)



