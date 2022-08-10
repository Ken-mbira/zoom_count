import pathlib
import os
from datetime import datetime
import tkinter.messagebox as messagebox

def is_csv(file_path:str) -> bool:
    if pathlib.Path(file_path).suffix == '.csv':
        return True
    
    return False


def check_if_new_file() -> bool:
    latest_file_path = ""
    try:
        latest_file = {}
        for file_path in os.scandir('staging'):
            if is_csv(file_path):
                if len(latest_file) == 0:
                    latest_file[file_path] = datetime.fromtimestamp(os.stat(file_path).st_ctime) #set the latest file to the latest file dict
                else:
                    current_date_time = datetime.fromtimestamp(os.stat(file_path).st_ctime)
                    if current_date_time > list(latest_file.values())[0]:
                        latest_file.clear()
                        latest_file[file_path] = datetime.fromtimestamp(os.stat(file_path).st_ctime)
            
        if len(latest_file) != 0:
            latest_file_path = list(latest_file.keys())[0]

    except FileNotFoundError:
        messagebox.showwarning('Zoom Count Error', 'There is no staging folder in this directory!')
        raise Exception("There is not staging folder in this directory")

    try:

        with open("already_read.txt","r") as already_read:
            file_already_read = False
            for line in already_read:
                line = line.removesuffix("\n")
                if line == latest_file_path.name:
                    file_already_read = True

    except FileNotFoundError:
        open("already_read.txt","w")
        return False

    if file_already_read == False:
        with open("already_read.txt","a") as write_already_read:
            write_already_read.write(f"{latest_file_path.name}\n")
        return True