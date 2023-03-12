import os
from os.path import abspath, join, getsize

sizes = {}

def determine():
    for top_dir, directories, files in os.walk('.'):
        for _file in files:
            full_path = abspath(join(top_dir, _file))
            size = getsize(full_path)
            sizes[full_path] = size

    items_shown = 0

    for path, size in sorted(sizes.items(), key=lambda x:x[1], reverse=True):
        if items_shown == 20:
            break
        print(f"Size: {size} Path: {path}")
        items_shown += 1

if __name__ == '__main__':
    determine()

    




