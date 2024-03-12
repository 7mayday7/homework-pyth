import os
from collections import namedtuple

# Создаем именованный кортеж для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_files_info(dir_path):
    files_info = []
    parent_dir = os.path.basename(os.path.dirname(dir_path))

    for entry in os.scandir(dir_path):
        file_name, file_extension = os.path.splitext(entry.name)
        is_directory = entry.is_dir()

        file_info = FileInfo(
            name=file_name if not is_directory else entry.name,
            extension=file_extension if not is_directory else '',
            is_directory=is_directory,
            parent_directory=parent_dir
        )
        files_info.append(file_info)

    return files_info

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory path.")
        sys.exit(1)

    files_info = get_files_info(directory_path)
    for file_info in files_info:
        print(file_info)