ERROR_MSG_PAIR_NUM = "Invalid input. Please insert the number of key-value pairs."
ERROR_MSG_KEY = "Invalid key input. Please input a valid key (latin letter)."
ERROR_MSG_VALUE = "Invalid value input. Please input a valid value (number)."
ERROR_MSG_DUP_KEYS =  "This key already exists. Please input distinct key."

def get_keys_and_values():
    try:
        num_of_pairs = int(input(f"Input number of key-value pairs you will store: "))
    except ValueError:
        print(ERROR_MSG_PAIR_NUM)
        return None

    result_string = ""
    added_keys = set()

    if num_of_pairs == 0:
        print('Cannot create a dictionary with 0 pairs')
        return None

    for i in range(num_of_pairs):
        while True:
            try:
                key = str(input(f"Input your {i+1} key (latin letter): "))
                if not key.isalpha():
                    print(ERROR_MSG_KEY)
                    return None
                if key in added_keys:
                    print(ERROR_MSG_DUP_KEYS)
                    return None
                added_keys.add(key)
                result_string += key
                break
            except ValueError:
                print(ERROR_MSG_KEY)

        while True:
            try:
                value = int(input(f"Input your {i+1} value (number): "))
                result_string += f" {value}, "
                break
            except ValueError:
                print(ERROR_MSG_VALUE)

    return result_string.strip(', ')

def create_dictionary(keys_and_values_str):

    if not keys_and_values_str is None:
        key_value_pairs = [pair.strip() for pair in keys_and_values_str.split(',')]

        result_dictionary = {}
        for pair in key_value_pairs:
            key, value = pair.split()
            result_dictionary[key] = int(value)
        return result_dictionary

keys_and_values = get_keys_and_values()
dictionary = create_dictionary(keys_and_values)
print("Dictionary:", dictionary)

