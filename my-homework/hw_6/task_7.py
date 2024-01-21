def is_list_empty(input_list):
    if input_list == []:
        return True

def is_list_of_integers(input_list):
    if not isinstance(input_list, list):
        return False

    for item in input_list:
        if not isinstance(item, int):
            return False

    return True

def count_students_above_average(input_list):
    if is_list_empty(input_list):
        print("Empty list")
        return []

    if not is_list_of_integers(input_list):
        print(f"Incorrect input {input_list}. Only list of integers is allowed")
        return []

    average_height = sum(input_list) / len(input_list)
    students_qty_above_avg_height = sum(1 for height in input_list if height > average_height)

    return students_qty_above_avg_height

def test(test_data, exp_res):
    act_res = count_students_above_average(test_data)
    print(f"Test: {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

if __name__ == "__main__": #to avoid test execution when import function from this file to task_8.py
    test_data = [182, 161, 175]
    exp_res = 2
    test(test_data, exp_res)

    test_data = [175, 175]
    exp_res = 0
    test(test_data, exp_res)

    test_data = []
    exp_res = []
    test(test_data, exp_res)