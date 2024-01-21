from task_2 import is_tuple
from task_3 import is_empty

def is_value_int(input_value):
    for value in input_value:
        if not isinstance(value, int):
            print("Contains not only integers")
            return False
    return True

def sum_of_even_numbers(input_tuple):
    if is_tuple(input_tuple) and is_value_int(input_tuple) and not is_empty(input_tuple, 'Tuple'):
        even_sum = 0
        for number in input_tuple:
            if number % 2 == 0:
                even_sum += number
        print(f"Sum of even numbers is {even_sum}")
        return even_sum

def test(test_data, exp_res):
    act_res = sum_of_even_numbers(test_data)
    print(f"Test: {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

if __name__ == "__main__": #to avoid test execution when import function
    # valid data
    test_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    exp_res = 30
    test(test_data, exp_res)

    # tuple of odds
    test_data = (1, 3, 5, 7, 9)
    exp_res = 0
    test(test_data, exp_res)

    # empty tuple
    test_data = ()
    exp_res = None
    test(test_data, exp_res)

    # not a tuple
    test_data = [[], {"key":"value"}, {0,2}, 'str', 3.14, 100, None, False]
    for i in range(len(test_data)):
        test(test_data[i], exp_res)