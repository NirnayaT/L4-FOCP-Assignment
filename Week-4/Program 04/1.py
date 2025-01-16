def validate_range(number):
    return 0 <= number <= 100

def test_validate():
    test_numbers = [-1, 0, 50, 100, 101]
    for num in test_numbers:
        print(f"{num} is {validate_range(num)}")

test_validate()