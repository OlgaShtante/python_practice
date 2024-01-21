def create_multiples_list():
    multiples_list = [num for num in range(1, 100 + 1) if num % 3 == 0 or num % 5 == 0]
    return multiples_list

print(create_multiples_list())

def test(exp_res):
    act_res = create_multiples_list()
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

exp_res = [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84,
 85, 87, 90, 93, 95, 96, 99, 100]
test(exp_res)