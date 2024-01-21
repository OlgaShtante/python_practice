from task_2 import is_tuple
from task_3 import is_empty
from task_4 import is_value_int
def get_index_and_value_of_max_number(input_tuple):
    if is_tuple(input_tuple) and is_value_int(input_tuple) and not is_empty(input_tuple, 'Tuple'):

        max_value = input_tuple[0]
        max_value_index = 0

        for number in input_tuple:
            if number >= max_value:
                max_value = number

                for i in range(1, len(input_tuple)):
                    if input_tuple[i] >=max_value:
                        max_value_index =i

        print(f"Maximum number {max_value} has index {max_value_index}")
        return max_value, max_value_index

def test(test_data, exp_res):
    act_res = get_index_and_value_of_max_number(test_data)
    print(f"Test: {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

# valid data
test_data = (-1, -4, 0)
exp_res = (0, 2)
test(test_data, exp_res)

# tuple len 1
test_data = (0,)
exp_res = (0, 0)
test(test_data, exp_res)

# not int
test_data = ('A', [6,8], {2,5}, 4, True, None)
exp_res = None
test(test_data, exp_res)

# not tuple
test_data =  '1, 2, 3'
test(test_data, exp_res)

