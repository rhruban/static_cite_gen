import os
import shutil

from copystatic import copy_files_recursive
from html_to_page import generate_page

static_path = "./static"
public_path = "./public"


def main():
    print("Deleting public directory")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("Copying files from static to public")
    copy_files_recursive(static_path, public_path)

    print("Generating Page")
    generate_page('content/index.md','template.html','public/index.html')

if __name__ == "__main__":
    main()
