def count_case_letters(text):
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    return upper, lower

def test_counter():
    text = "Hello World!"
    upper, lower = count_case_letters(text)
    print(f"Uppercase: {upper}, Lowercase: {lower}")
    
test_counter()