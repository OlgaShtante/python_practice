def is_palindrome(num):
    return str(num) == str(num)[::-1]

def create_palindrome_list():
    palindrome_list = [num for num in range(1, 100+1) if is_palindrome(num)]
    return palindrome_list

print(create_palindrome_list())

def test(exp_res):
    act_res = create_palindrome_list()
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

exp_res = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
test(exp_res)