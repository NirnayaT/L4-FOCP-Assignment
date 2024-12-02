import sys
import shutil

if len(sys.argv) > 1:
    source = sys.argv[1]
    backup = source + '.backup'
    try:
        shutil.copy2(source, backup)
        print(f"Backup created: {backup}")
    except:
        print("Error creating backup")
else:
    print("Please provide a filename")
