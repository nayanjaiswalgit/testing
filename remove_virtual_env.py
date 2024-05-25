import os
import shutil

def remove_virtual_envs(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name in ["venv", "env", "virtualenv"]:
                env_path = os.path.join(root, dir_name)
                print(f"Removing virtual environment: {env_path}")
                shutil.rmtree(env_path)

if __name__ == "__main__":
    folder_path = input("Enter the folder path where you want to remove virtual environments: ")
    if os.path.exists(folder_path):
        remove_virtual_envs(folder_path)
        print("Virtual environment directories removed successfully.")
    else:
        print("Invalid folder path.")
