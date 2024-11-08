import os
import shutil
import logging
from datetime import datetime
import threading

now = datetime.now()
script_run_time =now.strftime("%d_%m_%Y_%H_%M_%S") 

#logging
log_file = os.path.expanduser(f"~/file_move_log_{script_run_time}.log")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

#move from
download_folder = os.path.expanduser("~/Downloads")
#move to 
pictures_folder = os.path.expanduser("~/Pictures")
videos_folder = os.path.expanduser("~/Videos")
documents_folder = os.path.expanduser("~/Documents")
music_folder = os.path.expanduser("~/Music")

file_types = {
    documents_folder : ['.pdf', '.doc', '.docx', '.xls', 'xlsx', '.csv', '.pptx', '.txt'],
    videos_folder : ['.mp4', '.mkv', '.avi', '.mov', '.wmv'],
    music_folder : ['.mp3', '.wav', '.ogg'],
    pictures_folder : ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
}


file_classification = {}
with os.scandir(download_folder) as directory:
    for item in directory:
        if item.is_file():
            ext = os.path.splitext(item)[-1].lower()

            for folder, extension in file_types.items():
                # print(folder)
                if ext in extension:
                    # print(ext)
                    if folder not in file_classification:
                        file_classification[folder] = []
                    file_classification[folder].append(item.path)
#print(file_classification)

def move_file(source, destination):
    try:
        # shutil.move(source,destination)
        logger.info(f"moved {source} to {destination}")
    except Exception as e:
        logger.error(f"Error moving {source} to {destination}: {e}")

threads = []
for folder, files in file_classification.items():
    for file in files:
        thread = threading.Thread(target=move_file, args=(file,folder))
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()
