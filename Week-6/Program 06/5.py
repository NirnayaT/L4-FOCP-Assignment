import random
import string

def interval_encrypt(message):
    interval = random.randint(2, 20)
    result = [''] * (len(message) * interval)
    
    for i, char in enumerate(message):
        result[i * interval] = char
    
    # Fill gaps with random letters
    for i in range(len(result)):
        if not result[i]:
            result[i] = random.choice(string.ascii_lowercase)
    
    return (''.join(result), interval)

print(interval_encrypt("Hello World")) #output maybe: ('Hfeelfllov yWdojrulwdi', 2)