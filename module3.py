from module1 import write_to_file
from module2 import read_from_file

# Writes to a csv file and then reads and prints out its content
def create_and_read() -> None:
    content = []
    for line_number in range(0,10):
        content.insert(line_number, [line_number + 1, 'This is line {}'.format(line_number + 1)])
    write_to_file(content, 'my_file.csv')
    read_from_file('my_file.csv')

create_and_read()