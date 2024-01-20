def print_value_for_key(dictionary, key):
    return dictionary.get(key, "Key not found")

try:
    input_dict = eval(input("Enter dictionary, e.g., {'k1': 1, 'k2': 2}: "))
    input_key = input("Enter key: ")
    result = print_value_for_key(input_dict, input_key)
    print(result)
except Exception as error_msg:
    print(f"Invalid input. Error: {error_msg}")

def test(test_dict, test_key, exp_res):
    act_res = print_value_for_key(test_dict, test_key)
    print(f"Test: {test_dict}, {test_key} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

# valid data
test_dict = {'a': 1, 'b': 2, 'c': 3}
test_key = 'b'
exp_res = 2
test(test_dict, test_key, exp_res)

# wrong key
test_dict = {'a': 1, 'b': 2, 'c': 3}
test_key = 'd'
exp_res = "Key not found"
test(test_dict, test_key, exp_res)
