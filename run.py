from datetime import datetime
import os

# local modules
import helpers
import text

import tkinter.messagebox as messagebox

import pandas as pd
from decouple import config

def main():
    latest_file_path : str = ""

    try:
        latest_file = {}
        for file_path in os.scandir('staging'):
            if helpers.is_csv(file_path):
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

    if(latest_file_path) != "":
        attendance_dict = {}

        report_df = pd.read_csv(
            latest_file_path,
            names=['#','user','email','date_submitted','attendance'],
            parse_dates=['date_submitted'],
            skiprows=8,
            usecols=['user','email','date_submitted','attendance']
        )

        for _,row in report_df.iterrows():
            if row['user'] in list(attendance_dict.keys()):
                if int(attendance_dict.get(row['user'])) > int(row['attendance']):
                    continue
                else:
                    attendance_dict[row['user']] = row['attendance']
            else:
                attendance_dict[row['user']] = int(row['attendance'])

        if len(attendance_dict) != 0:
            total_attendance = 0
            for i in list(attendance_dict.values()):
                total_attendance += int(i)

            receiver_number = config("RECEIVER_NUMBER")

            try:
                my_text = text.Text()
                my_text.send_text(receiver_name="Ken Mbira",receiver_number=receiver_number,zoom_attendance=total_attendance)
            except:
                pass


if __name__ == '__main__':  
    main()