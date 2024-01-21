def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def create_dictionary():
    return {i: factorial(i) for i in range(1, 11)}

print(create_dictionary())

def test(exp_res):
    act_res = create_dictionary()
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

exp_res ={1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880, 10: 3628800}
test(exp_res)