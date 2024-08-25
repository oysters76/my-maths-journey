"""
 Generates a simple static HTML page to showcase my math's journey 
"""
import os 

LOG_TYPES = ["ERROR","WARN","LOG"] 
ROOT_FOLDERS = ["algebra"]

def log(saywhat, level=2):
    s = f"[{LOG_TYPES[level]}]:{saywhat}" 
    print(s)

def is_folder(potential_folder):
    return os.path.isdir(potential_folder)
    
def process_folder(folder_path):
    stack = [folder_path]
    
    while len(stack) > 0:
        folder = stack.pop() 
        log(f"processing folder: {folder}")
        inside_folders = os.listdir(folder) 
        for inside_folder in inside_folders:
            potential_folder = os.path.join(folder, inside_folder)
            if (is_folder(potential_folder)):
                stack.append(potential_folder)
        


all_folders = os.listdir(".")

for f in all_folders:
    if f not in ROOT_FOLDERS:
        log(f + " folder was rejected")
        continue 
    process_folder(os.path.join(".", "algebra"))
    

