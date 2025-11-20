import os
import shutil

from block_markdown import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("Error No Title")


def generate_page(from_path, template_path, dest_path,basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown = file.read()
    with open(template_path, 'r') as file:
        template = file.read()
    html_nodes = markdown_to_html_node(markdown)
    html = html_nodes.to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}",title).replace("{{ Content }}", html)
    page = page.replace('href="/', 'href="{basepath}').replace('src="/', 'src="{basepath}')
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for file in os.listdir(dir_path_content):
        start = os.path.join(dir_path_content, file)
        # TODO file from .md to .html
        end = os.path.join(dest_dir_path, file.replace('.md','.html'))
        print(f" - {start} to {end} using {template_path}")
        if os.path.isfile(start):
            generate_page(start,template_path,end,basepath)
        else:
            generate_pages_recursive(start,template_path,end,basepath)


