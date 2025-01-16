import sys

def grep_command(pattern, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line.rstrip())
    except FileNotFoundError:
        print(f"File {filename} not found")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep_command.py pattern filename")
    else:
        grep_command(sys.argv[1], sys.argv[2])
#Output:
# python 3.py Nirnaya  file1.txt
#     My name is Nirnaya