DICTIONARY = {')': '(', '}': '{', ']': '['}

def is_valid_char(str):
    new_list = []

    for char in str:
        if char in DICTIONARY.values():
            new_list.append(char)
        elif char in DICTIONARY.keys():
            if not new_list or new_list.pop() != DICTIONARY[char]:
                return False
        else:
            return False

    return not new_list


test_data = ["()", "()[]{}", "(]", "(){}}{", "([)]", "([])"]

for str in test_data:
    print(f"The string '{str}' is {'valid' if is_valid_char(str) else 'not valid'}.")