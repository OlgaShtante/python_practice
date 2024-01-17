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


def test(testData, exp_res):
    act_res = find_min_and_max_numbers(testData)
    print(f"Test data {testData} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

testData = [ 1, 0, 1000]
exp_res = (0, 1000)
test(testData, exp_res)

testData = (0, -1, -1000)
exp_res = (-1000, 0)
test(testData, exp_res)

testData = ['1', 2]
exp_res = (None)
test(testData, exp_res)

testData = 'string'
exp_res = (None)
test(testData, exp_res)

testData = []
exp_res = (None)
test(testData, exp_res)

testData = {}
exp_res = (None)
test(testData, exp_res)

testData = ()
exp_res = (None)
test(testData, exp_res)

testData = 1
exp_res = (None)
test(testData, exp_res)