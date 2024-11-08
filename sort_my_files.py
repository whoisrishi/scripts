import os
import shutil

download_folder = os.path.expanduser("~/Downloads")
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

import threading
def move_file(source, destination):
    shutil.move(source,destination)

threads = []
for folder, files in file_classification.items():
    for file in files:
        thread = threading.Thread(target=move_file, args=(file,folder))
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()
