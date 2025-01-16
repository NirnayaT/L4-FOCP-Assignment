import sys

def wc_command(filename):
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            chars = len(content)
            
        with open(filename, 'r') as file:
            lines = 0
            words = 0
            for line in file:
                lines += 1
                words += len(line.split())
            
            print(f"Lines: {lines}")
            print(f"Words: {words}")
            print(f"Characters: {chars}")
    except FileNotFoundError:
        print(f"File {filename} not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc_command.py filename")
    else:
        wc_command(sys.argv[1])
#output:
# python 4.py file1.txt
#   Lines: 3
#   Words: 10
#   Characters: 47