import csv
from datetime import datetime
import os
from socket import timeout
import subprocess

import helpers

import tkinter as tk
import tkinter.messagebox as messagebox

def main():
    latest_file_path = ""

    try:
        latest_file = {}
        for file_path in os.scandir('staging'):
            if helpers.is_csv(file_path):
                if len(latest_file) == 0:
                    latest_file[file_path.name] = datetime.fromtimestamp(os.stat(file_path).st_ctime) #set the latest file to the latest file dict
                else:
                    current_date_time = datetime.fromtimestamp(os.stat(file_path).st_ctime)
                    if current_date_time > list(latest_file.values())[0]:
                        latest_file.clear()
                        latest_file[file_path.name] = datetime.fromtimestamp(os.stat(file_path).st_ctime)

        latest_file_path = list(latest_file.keys())[0]

    except FileNotFoundError:
        messagebox.showwarning('Zoom Count Error', 'There is no staging folder in this directory!')


if __name__ == '__main__':  
    main()