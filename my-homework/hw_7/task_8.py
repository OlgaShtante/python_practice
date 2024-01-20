def combine_dictionaries(dict_1, dict_2):
    combined_dict = dict_1.copy()
    combined_dict.update(dict_2)
    return combined_dict

try:
    dict1 = eval(input("Enter the 1st dictionary, e.g., {'k1': 1, 'k2': 2 }: "))
    dict2 = eval(input("Enter the 2nd dictionary, e.g., {'k1': 1, 'k2': 2 }: "))
    combined_dictionary = combine_dictionaries(dict1, dict2)
    print("Combined dictionary:", combined_dictionary)
except Exception as error_msg:
    print(f"Invalid input. Error: {error_msg}")

def test(test_dict_1, test_dict_2, exp_res):
    act_res = combine_dictionaries(test_dict_1, test_dict_2)
    print(f"Test: {test_dict_1}, {test_dict_2} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

# valid data
test_dict_1 = {'a': 1, 'b': 2, 'c': 3}
test_dict_2 = {'b': 4, 'd': 5}
exp_res = {'a': 1, 'b': 4, 'c': 3, 'd': 5}
test(test_dict_1, test_dict_2, exp_res)