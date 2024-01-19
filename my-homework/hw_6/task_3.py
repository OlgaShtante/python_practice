from collections.abc import Iterable
def find_min_and_max_numbers(list_of_numbers):
    if not isinstance(list_of_numbers, Iterable):
        print(f"{list_of_numbers} is not iterable")
        return None

    if not list_of_numbers:
        print(f"{list_of_numbers} is empty")
        return None

    min_value = max_value = list_of_numbers[0]

    for number in list_of_numbers:
        if not type(number) is int:
            print(f"{number} is not integer in {list_of_numbers}")
            return None
        if number < min_value:
            min_value = number
        elif number > max_value:
            max_value = number

    return min_value, max_value

def test(test_data, exp_res):
    act_res = find_min_and_max_numbers(test_data)
    print(f"Test data {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

test_data = [ 1, 0, 1000]
exp_res = (0, 1000)
test(test_data, exp_res)

test_data = (0, -1, -1000)
exp_res = (-1000, 0)
test(test_data, exp_res)

test_data = ['1', 2]
exp_res = (None)
test(test_data, exp_res)

test_data = 'string'
test(test_data, exp_res)

test_data = []
test(test_data, exp_res)

test_data = {}
test(test_data, exp_res)

test_data = ()
test(test_data, exp_res)

test_data = 1
test(test_data, exp_res)