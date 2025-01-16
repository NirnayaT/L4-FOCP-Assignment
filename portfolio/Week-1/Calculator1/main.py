class Calculator():
    def add(n1, n2):
        return n1 + n2

    def substract(n1, n2):
        return n1 - n2

    def division(n1, n2):
        return n1 / n2

    def multiply(n1, n2):
        return n1 * n2

    def floordivision(n1, n2):
        return n1 // n2

    def exponential(n1, n2):
        return n1**n2


print("****WELCOME TO CACLUCLATOR CLI****")
print("Choose an action to perform.")
print("1. Addition")
print("2. Substraction")
print("3. Division")
print("4. Multiplication")
print("5. Floor-Divison")
print("6. Exponential")

num = int(input("Enter the number: "))

if num == 1:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    value = Calculator.add(n1, n2)
    print("Addition:", value)
elif num == 2:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print("Substraction:", Calculator.substract(n1, n2))
elif num == 3:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: ")  )
    print("Division:", Calculator.division(n1, n2))
elif num == 4:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print("Addition", Calculator.multiply(n1, n2))
elif num == 5:
    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")
    print("Addition", Calculator.floordivision(n1,n2))
elif num == 6:
    n1 = input("Enter the first number: ")
    n2 = input("Enter the second number: ")
    print("Addition", Calculator.exponential(n1,n2))
