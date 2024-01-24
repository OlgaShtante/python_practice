def sum_of_squares_generator(n):
    n = abs(n)
    current_sum = 0
    for number in range(1, n + 1):
        current_sum += number**2
        print(f"Sum of squares of all numbers up to {number}: {current_sum}")
        yield current_sum

def test(test_data, exp_res):
    act_res = []
    for sum in sum_of_squares_generator(test_data):
        act_res.append(sum)
    assert act_res == exp_res, f"Actual result {act_res} does not match {exp_res}"


test_data = -10
exp_res = [1, 5, 14, 30, 55, 91, 140, 204, 285, 385]
test(test_data, exp_res)


