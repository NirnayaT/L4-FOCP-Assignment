import sys

def diff_command(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
            if content1 == content2:
                print("Files are same")
            else:
                print("Files are different")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff_command.py file1 file2")
    else:
        diff_command(sys.argv[1], sys.argv[2])
