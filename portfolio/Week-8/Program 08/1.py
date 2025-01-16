import sys

def nl_command(filename):
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                print(f"{line_num:6d}\t{line}", end='')
    except FileNotFoundError:
        print(f"File {filename} not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl_command.py filename")
    else:
        nl_command(sys.argv[1])
#output:
# python 1.py file1.txt
    #  1  Hello World
    #  2  This is a test
    #  3  My name is Nirnaya