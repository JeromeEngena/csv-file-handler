import csv

# Create a csv file and write to it
def write_to_file(content: list = [''], file_name: str = 'file.csv') -> None:
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(content)