number = int(input("Enter a number between 0 and 12 for the times table: "))
if 0 <= number <= 12:
    for i in range(13):
        print(f"{i} x {number} = {i * number}")
else:
    print("Error: Please enter a number between 0 and 12.")
