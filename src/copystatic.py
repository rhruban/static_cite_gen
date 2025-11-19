import os
import shutil


def copy_files_recursive(source_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for file in os.listdir(source_path):
        start = os.path.join(source_path, file)
        end = os.path.join(dest_path, file)
        print(f" - {start} to {end}")
        if os.path.isfile(start):
            shutil.copy(start, end)
        else:
            copy_files_recursive(start, end)
