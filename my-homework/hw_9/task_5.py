from typing import List, Union

def count_sum_of_list_values(lst: List[Union[int, List]]) -> int:
    total_sum = 0
    for item in lst:
        if isinstance(item, list):
            total_sum += count_sum_of_list_values(item)
        elif isinstance(item, int):
            total_sum += item
    return total_sum


def test(test_data, exp_res):
    try:
        act_res= count_sum_of_list_values(test_data)
        act_res == exp_res, f"Error: {act_res} does not match expected result {exp_res}"
        print(act_res)
    except TypeError as error_msg:
        print(f"Error: {error_msg}")


# happy path
test_data = [0, [1, 2, [3, 4, 5, [6, 7, 8, 9]]]]
exp_res = 45
test(test_data, exp_res)

test_data = [(0,1), {1, 2}, "Test", False, None, {"a":1}]
exp_res = 0
test(test_data, exp_res)