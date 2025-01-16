def remove_last_char(text):
    return text[:-1] if len(text) > 1 else text

def test_trimmer():
    tests = ["Hello", "A", ""]
    for test in tests:
        print(f"'{test}' -> '{remove_last_char(test)}'")
        
test_trimmer()