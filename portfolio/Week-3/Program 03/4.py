bad_word = ["password", "letmein", "sesame", "hello", "justinbieber"]
password = input("enter your password(between 8 to 12 words): ")
if len(password) < 8 or len(password) > 12:
    print("error: the password is not between the required length")
elif password.lower() in bad_word:
    print("error: invalid character")

password2 = input("enter again: ")
if password == password2:
    print("password successfully set")
else:
    print("password donot match")
