import os

def remove_empty_folders_and_ino_files(root_folder):
    # Walk through the directory tree
    for foldername, subfolders, filenames in os.walk(root_folder, topdown=False):
        try:
            # Check if the current folder is empty
            if not os.listdir(foldername):
                # Remove the empty folder
                print("Removing empty folder:", foldername)
                os.rmdir(foldername)
            else:
                # Check if any .ino files exist and remove them
                for filename in filenames:
                    if filename.endswith(".ino"):
                        file_path = os.path.join(foldername, filename)
                        print("Removing .ino file:", file_path)
                        os.remove(file_path)
        except PermissionError as e:
            print("Permission error:", e)
            continue

if __name__ == "__main__":
    root_folder = input("Enter the root folder path: ")
    remove_empty_folders_and_ino_files(root_folder)
    print("Empty folders and .ino files removed successfully.")
