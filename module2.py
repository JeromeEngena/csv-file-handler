import os.path
import csv

# Checks for presence of a csv file and if present, reads and prints its content
def read_from_file(file_name: str = 'file.csv') -> None:
    if (os.path.exists(file_name)):
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print(file_name, ' does not exist!')