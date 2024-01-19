from math import gcd
ERROR_MSG = "Invalid input. Only integers are allowed."

def calculate_gcd():
    try:
        num1 = int(input("Enter the 1st number: "))
    except ValueError:
        print(ERROR_MSG)
        return []
    try:
        num2 = int(input("Enter the 2nd number: "))
    except ValueError:
        print(ERROR_MSG)
        return []

    return gcd(num1, num2)

result = calculate_gcd()
print(f"The greatest common divisor: {result}")