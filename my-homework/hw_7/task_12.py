def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
def create_divisors_dictionary():
    return {i: get_divisors(i) for i in range(1, 10 + 1)}

print(create_divisors_dictionary())

def test(exp_res):
    act_res = create_divisors_dictionary()
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

exp_res ={1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5], 6: [1, 2, 3, 6], 7: [1, 7], 8: [1, 2, 4, 8], 9: [1, 3, 9], 10: [1, 2, 5, 10]}
test(exp_res)