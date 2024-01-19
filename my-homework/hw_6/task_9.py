from task_7 import is_list_empty

def is_list_of_str(input_list):
    if is_list_empty(input_list):
        return False

    if not isinstance(input_list, list):
        return False

    for item in input_list:
        if not isinstance(item, str):
            return False

    return True

def longest_common_prefix(input_list):
    if not is_list_of_str(input_list):
        print("Invalid input")
        return ""

    input_list.sort()

    first_str = input_list[0]
    last_str = input_list[-1]

    common_prefix = ""
    for i in range(len(first_str)):
        if first_str[i] == last_str[i]:
            common_prefix += first_str[i]
        else:
            break

    return common_prefix

def test(test_data, exp_res):
    act_res = longest_common_prefix(test_data)
    print(f"Test: {test_data} returns '{act_res}'")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

test_data = ['flight', 'flow', 'flower']
exp_res = 'fl'
test(test_data, exp_res)

test_data = ['car', 'dog', 'racecar']
exp_res = ''
test(test_data, exp_res)

test_data = ''
test(test_data, exp_res)

test_data = []
test(test_data, exp_res)

test_data = [1, 2]
test(test_data, exp_res)
