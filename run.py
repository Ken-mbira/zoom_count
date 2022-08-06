import csv
from datetime import datetime
import os

import helpers

def main():
    todays_date = datetime.today().strftime('%d %B %Y')

    try:
        for file_name in os.scandir('staging'):
            if helpers.is_csv(file_name):
                print(file_name)

    except FileNotFoundError as e:
        print(e.strerror)
    # with open('staging/July17.csv',mode='r') as my_file:
    #     for row in my_file:
    #         print(row)

if __name__ == '__main__':  
    main()