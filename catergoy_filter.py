import os
import shutil
import logging

def move_files(root_dir):
    image_dir = os.path.join(root_dir, 'Filteredimages')
    video_dir = os.path.join(root_dir, 'Filtedvideos')
    already_dir = os.path.join(root_dir, 'already')

    # Create directories if they don't exist
    os.makedirs(image_dir, exist_ok=True)
    os.makedirs(video_dir, exist_ok=True)
    os.makedirs(already_dir, exist_ok=True)

    # Configure logging
    logging.basicConfig(filename='file_mover.log', level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            # Check if the file is an image
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                source_path = os.path.join(foldername, filename)
                destination_path = os.path.join(image_dir, filename)
                if not os.path.exists(destination_path):
                    try:
                        shutil.move(source_path, destination_path)
                        print(f"Moved {filename} to images folder")
                    except Exception as e:
                        logging.error(f"Failed to move {filename}: {str(e)}")
                        print(f"Failed to move {filename}: {str(e)}")
                else:
                    print(f"{filename} already exists in images folder")
                    already_destination = os.path.join(already_dir, filename)
                    shutil.move(source_path, already_destination)
                    print(f"Moved {filename} to already folder")

            # Check if the file is a video
            elif filename.lower().endswith(('.mp4', '.avi', '.mkv')):
                source_path = os.path.join(foldername, filename)
                destination_path = os.path.join(video_dir, filename)
                if not os.path.exists(destination_path):
                    try:
                        shutil.move(source_path, destination_path)
                        print(f"Moved {filename} to videos folder")
                    except Exception as e:
                        logging.error(f"Failed to move {filename}: {str(e)}")
                        print(f"Failed to move {filename}: {str(e)}")
                else:
                    print(f"{filename} already exists in videos folder")
                    already_destination = os.path.join(already_dir, filename)
                    shutil.move(source_path, already_destination)
                    print(f"Moved {filename} to already folder")

if __name__ == "__main__":
    root_directory = input("Enter the root directory: ")
    move_files(root_directory)
