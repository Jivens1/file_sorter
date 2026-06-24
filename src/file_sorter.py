import os
import shutil

# WHERE to look
folder_path = r"C:\PAITOON\file_sorter\test"

# CREATE the destination folders (if they don't exist)
os.makedirs(os.path.join(folder_path, "Images"), exist_ok=True)
os.makedirs(os.path.join(folder_path, "Documents"), exist_ok=True)
os.makedirs(os.path.join(folder_path, "Music"), exist_ok=True)
os.makedirs(os.path.join(folder_path, "Presentations"), exist_ok=True)

# GET all items in the folder
all_items = os.listdir(folder_path)


for item in all_items:
    #  SKIP if it's a folder
    full_path = os.path.join(folder_path, item)
    if os.path.isdir(full_path):
        continue
    
    #  CHECK the file type and MOVE it
    if item.endswith((".jpg", ".PNG", ".png", ".gif")):
        destination = os.path.join(folder_path, "Images", item)
        shutil.move(full_path, destination)
        print(f"[MOVED] {item} -> Images/")
    
    elif item.endswith((".pdf", ".docx", ".txt")):
        destination = os.path.join(folder_path, "Documents", item)
        shutil.move(full_path, destination)
        print(f"[MOVED] {item} -> Documents/")
    
    elif item.endswith((".mp3", ".wav")):
        destination = os.path.join(folder_path, "Music", item)
        shutil.move(full_path, destination)
        print(f"[MOVED] {item} -> Music/")
    
    elif item.endswith(".pptx"):
        destination = os.path.join(folder_path, "Presentations", item)
        shutil.move(full_path, destination)
        print(f"[MOVED] {item} -> Presentations/")
    
    else:
        print(f"[IGNORED] {item}")
