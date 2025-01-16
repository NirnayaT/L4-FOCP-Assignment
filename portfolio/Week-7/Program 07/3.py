def manage_capitals():
    capitals = {}
    
    while True:
        country = input("Enter a country name (or 'quit' to exit): ").lower()
        
        if country == 'quit':
            break
            
        if country in capitals:
            print(f"The capital of {country.title()} is {capitals[country]}")
        else:
            capital = input(f"I don't know the capital of {country.title()}. Please enter it: ")
            capitals[country] = capital
            print(f"Thank you! I've learned that the capital of {country.title()} is {capital}")

# Run the program
manage_capitals()
