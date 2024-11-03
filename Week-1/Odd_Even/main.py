def check_odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


try:
    number = int(input("Enter a number to check if it's odd or even: "))
    result = check_odd_even(number)
    print(f"The number {number} is {result}")
except ValueError:
    print("Please enter a valid integer number")


def check_multiple_numbers():
    while True:
        choice = input("\nWould you like to check another number? (yes/no): ").lower()
        if choice == "no":
            print("Thank you for using the odd/even checker!")
            break
        elif choice == "yes":
            try:
                number = int(input("Enter a number: "))
                result = check_odd_even(number)
                print(f"The number {number} is {result}")
            except ValueError:
                print("Please enter a valid integer number")
        else:
            print("Please enter 'yes' or 'no'")


check_multiple_numbers()
