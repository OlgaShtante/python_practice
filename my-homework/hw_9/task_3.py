def map_square(lst: list) -> list:
    result = list(map(lambda x: x**2, lst))
    print(result)
    return result


def test(test_data, exp_res):
    try:
        act_res= map_square(test_data)
        act_res == exp_res, f"Error: {act_res} does not match expected result {exp_res}"
    except TypeError as error_msg:
        print(error_msg)

# happy path
test_data = [1, 2, 3, 4, 5]
exp_res = [1, 4, 9, 16, 25]
test(test_data, exp_res)

test_data = [0, -10]
exp_res = [0, 100]
test(test_data, exp_res)

