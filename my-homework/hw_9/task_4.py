VOWELS = "aeiou"
def count_vowels(s: str, case_sensitive: bool = False) -> int:

    if case_sensitive:
        vowels = VOWELS+VOWELS.upper()
    else:
        s = s.lower()
        vowels = VOWELS

    distinct_chars = ''.join(sorted(set(s), key=s.index))
    return len([char for char in distinct_chars if char in vowels])


def test(s, case_sensitive, exp_res):
    try:
        act_res= count_vowels(s, case_sensitive)
        print(act_res)
        act_res == exp_res, f"Error: {act_res} does not match expected result {exp_res}"
    except TypeError as error_msg:
        print(f"Error: {error_msg}")


# happy path
test_data_str = "Hello, world!"
case_bool = False
exp_res = 2
test(test_data_str, case_bool, exp_res)

test_data_str = "HEeelloo, wOorld!"
case_bool = True
exp_res = 4
test(test_data_str, case_bool, exp_res)

test_data_str = ""
exp_res = 0
test(test_data_str, case_bool, exp_res)