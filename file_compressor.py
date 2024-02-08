#!/usr/bin/python3
""" Importing the necessary libraries """
import os
import zipfile
import tarfile
from datetime import datetime


def compress_folder(folder, compress_type):
    """ Compress the folder using the selected compressed file type """
    folder_name = os.path.basename(folder)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_name = f"{folder_name}_{timestamp}"

    if compress_type == ".zip":
        file_name += ".zip"
        try:
            with zipfile.ZipFile(file_name, "w") as zipf:
                for root, dirs, files in os.walk(folder):
                    for file in files:
                        zipf.write(os.path.join(root, file))
            print(f"Folder '{folder_name}' was compressed to '{file_name}' successfully")
        except Exception as e:
            print(f"An error occurred while compressing the folder: {e}")

    elif compress_type == ".tar" or compress_type == ".tgz":
        file_name += ".tar"
        if compress_type == ".tgz":
            file_name += ".gz"
        try:
            with tarfile.open(file_name, "w:gz" if compress_type == ".tgz" else "w") as tarf:
                tarf.add(folder, arcname=os.path.basename(folder))
            print(f"Folder '{folder_name}' was compressed to '{file_name}' successfully")
        except Exception as e:
            print(f"An error occurred while compressing the folder: {e}")
    else:
        print("Invalid compressed file type")

def main():
    """ Main function """
    folder = input("Enter path of the folder to compress: ")
    if not os.path.exists(folder):
        print("The folder does not exist")
        return
    
    compress_types = [".zip", ".tar", ".tgz"]
    print("Available compressed file types:")
    for i, compress_type in enumerate(compress_types, 1):
        print(f"{i}. {compress_type}")
    
    choice = int(input("Enter the number of the compressed file type to use: "))
    if choice <= 1 or choice <= len(compress_types):
        compress_type = compress_types[choice - 1]
        compress_folder(folder, compress_type)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()