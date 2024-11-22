number = int(input("Enter a number between -12 and 12 for the times table: "))
if -12 <= number <= 12:
    if number >= 0:
        for i in range(13):
            print(f"{i} x {number} = {i * number}")
    else:
        for i in range(12, -1, -1):
            print(f"{i} x {abs(number)} = {i * abs(number)}")
else:
    print("Error: Please enter a number between -12 and 12.")
