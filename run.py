import csv

def main():
    with open('staging/July17.csv',mode='r') as my_file:
        for row in my_file:
            print(row)

if __name__ == '__main__':
    main()