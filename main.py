from writer import write_to_file
from reader import read_from_file


# Writes to a csv file and then reads and prints out its content
def create() -> None:
    content = []
    for line_number in range(0, 10):
        content.insert(line_number, [line_number + 1, 'This is line {}'.format(line_number + 1)])
    write_to_file(content, 'my_file.csv')
    read_from_file('my_file.csv')


create()
