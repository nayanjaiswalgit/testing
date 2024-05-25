import os
import shutil

def is_react_project(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.js') or file.endswith('.tsx') or file.endswith('.ts') or file.endswith('.jsx'):
                return True
    return False

def move_react_projects(root_folder, destination_folder):
    for root, dirs, files in os.walk(root_folder):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if is_react_project(folder_path):
                destination_path = os.path.join(destination_folder, folder)
                shutil.move(folder_path, destination_path)
                print(f"Moved {folder} to {destination_path}")

if __name__ == "__main__":
    root_folder = input("Enter the root folder path: ")
    destination_folder = "/project123"  # Change this to your desired destination folder path
    move_react_projects(root_folder, destination_folder)
