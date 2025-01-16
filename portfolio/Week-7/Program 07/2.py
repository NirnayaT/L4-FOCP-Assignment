def letters_in_either(word1, word2):
    return sorted(set(word1.lower()) | set(word2.lower()))

def letters_in_both(word1, word2):
    return sorted(set(word1.lower()) & set(word2.lower()))

def letters_in_one_not_both(word1, word2):
    return sorted(set(word1.lower()) ^ set(word2.lower()))

# Test
print(letters_in_either("hello", "world"))      # ['d', 'e', 'h', 'l', 'o', 'r', 'w']
print(letters_in_both("hello", "world"))        # ['l', 'o']
print(letters_in_one_not_both("hello", "world")) # ['d', 'e', 'h', 'r', 'w']
