def get_divisors_set(n):
    if n == 0:
        return 'Any number'
    n = abs(n)

    possible_divisors= [i for i in range(1, n + 1)]
    actual_divisors_list = [i for i in possible_divisors if n % i == 0 ]
    divisors_set = set(actual_divisors_list)
    return divisors_set

try:
    user_input = int(input("Input number: "))
    result_set = get_divisors_set(user_input)
    print("Set of divisors:", result_set)
except Exception as error_msg:
    print(f"Invalid input. Error: {error_msg}")

def test(test_data, exp_res):
    act_res = get_divisors_set(test_data)
    print(f"Test: {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

# possitive number
test_data = 12
exp_res =  {1, 2, 3, 4, 6, 12}
test(test_data, exp_res)

# zero
test_data = 0
exp_res =  'Any number'
test(test_data, exp_res)

# negative number
test_data = -5
exp_res =  {1,5}
test(test_data, exp_res)