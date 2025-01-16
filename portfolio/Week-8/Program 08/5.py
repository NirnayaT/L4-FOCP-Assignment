import sys
import re

def load_dictionary(dict_path):
    with open(dict_path, 'r') as file:
        return set(word.strip().lower() for word in file)

def spell_check(filename, dictionary):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            # Split into words and remove punctuation
            words = re.findall(r'\b\w+\b', content)
            misspelled = [word for word in words if word not in dictionary]
            
            print("Misspelled words:")
            for word in misspelled:
                print(word)
    except FileNotFoundError:
        print(f"File {filename} not found")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python spell_command.py dictionary_file text_file")
    else:
        dictionary = load_dictionary(sys.argv[1])
        spell_check(sys.argv[2], dictionary)
#output:
# python 5.py words.txt spell_checker.txt
    # Misspelled words:
    # quik
    # brownn
    # jumpd
    # ovr
    # lazzy
    # dogg
    # whille
    # brekfast