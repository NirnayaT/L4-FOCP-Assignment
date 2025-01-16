import sys

if len(sys.argv) > 1:
    print(min(sys.argv[1:], key=len))
else:
    print("No arguments provided")
