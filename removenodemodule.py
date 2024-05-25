import os
import shutil

def remove_node_modules_and_env(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name == "node_modules":
                node_modules_path = os.path.join(root, dir_name)
                print(f"Removing node_modules: {node_modules_path}")
                shutil.rmtree(node_modules_path)
        for file_name in files:
            if file_name == ".env":
                env_file_path = os.path.join(root, file_name)
                print(f"Removing .env file: {env_file_path}")
                os.remove(env_file_path)

if __name__ == "__main__":
    folder_path = input("Enter the folder path where you want to remove node_modules and .env files: ")
    if os.path.exists(folder_path):
        remove_node_modules_and_env(folder_path)
        print("Node_modules directories and .env files removed successfully.")
    else:
        print("Invalid folder path.")
