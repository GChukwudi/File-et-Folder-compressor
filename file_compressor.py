# Write a Python program that allows users to compress files and folders to any compressed file type they choose (e.g., .zip, .tar, .tgz, etc.). When the user selects .tgz as their compress type, the archive or compressed files or folder should be saved as "name_of_the_folder_date_month_year."

# For example, if the user selects .tgz and the compressed folder is named "MyFolder," the compressed file should be saved as "MyFolder_2023_02_27.tgz".

# Your program should prompt the user to select the folder to compress and then display a list of available compressed file types. The user should be able to select the desired compressed file type from the list, and your program should compress the selected folder using the selected compressed file type.

# Your program should also display a message to the user indicating the success or failure of the compression process. If the compression process fails, your program should provide an error message explaining the cause of the failure.

# Assume the user has the necessary libraries and tools installed to perform the compression.

# Note: Consider using the tarfile library to create tar archives and the 

#  library to create zip archives. Also, ensure that there is a README file explaining how to run your code and the group members.

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