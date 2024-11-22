bad_words = ["password", "letmein", "sesame", "hello", "justinbieber"]

while True:
    password = input("Enter your password (between 8 to 12 characters): ")
    
    if len(password) < 8 or len(password) > 12:
        print("Error: The password must be between 8 and 12 characters")
        continue
        
    if password.lower() in bad_words:
        print("Error: Password contains invalid words")
        continue
        
    password2 = input("Enter password again: ")
    
    if password == password2:
        print("Password successfully set")
        break
    else:
        print("Passwords do not match")

