import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def copy_file(file_path, destination_folder):
    filename = os.path.basename(file_path)
    destination_file = os.path.join(destination_folder, filename)
    shutil.copy2(file_path, destination_file)
    print(f'File {filename} copy to {destination_folder}')

def copy_files(source_folder, destination_folder="dist"):
    # Check if the destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files = []
    # recursive traversal of folders
    for root, dirs, filenames in os.walk(source_folder):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)

    # ThreadPoolExecutor for copying files in parallel
    with ThreadPoolExecutor() as executor:
        executor.map(lambda file_path: copy_file(file_path, destination_folder), files)

def sort_files_by_extension(folder):
    
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1][1:]
            
            extension_folder = os.path.join(folder, file_extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)
            
            shutil.move(file_path, os.path.join(extension_folder, filename))
            print(f'Файл {filename} переміщено до {extension_folder}')

def main():
    source_folder = input("Enter the full path to the source folder: ")
    destination_folder = input("Enter the full path to the destination folder: ")
    
    if not destination_folder:
        print("The destination folder is not defined. By default, we will use the 'dist' folder")
        destination_folder = 'dist'

    copy_files(source_folder, destination_folder)
    sort_files_by_extension(destination_folder)

if __name__ == "__main__":
    main()
