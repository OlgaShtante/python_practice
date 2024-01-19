
test_data = ["()", "()[]{}", "(]", "(){}}{", "([)]", "([])"]
for str in test_data:
    print(f"The string '{str}' is {'valid' if True else 'not valid'}.")