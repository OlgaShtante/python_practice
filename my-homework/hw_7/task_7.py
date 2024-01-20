def print_value_for_key():
    try:
        input_dict = eval(input("Enter dictionary (e.g., {'a': 1, 'b': 2, 'c': 3}): "))
        input_key = input("Enter key: ")
        return input_dict.get(input_key, "Key not found")
    except Exception as error_msg:
        print(f"Invalid input. Error: {error_msg}")
        return None

result = print_value_for_key()
print(result)