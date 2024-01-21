def is_subset(set_1, set_2):
    if set_1.issubset(set_2) or set_2.issubset(set_1):
        return True
    else:
        return False

try:
    set1 = eval(input("Input the 1st set, e.g., {1, 2}: "))
    set2 = eval(input("Input the 2nd set, e.g., {1, 2, 3}: "))
    print(f"{'Yes' if is_subset(set1, set2) else 'No'}")
except Exception as error_msg:
    print(f"Invalid input. Error: {error_msg}")

def test(set_1, set_2, exp_res):
    act_res = is_subset(set_1, set_2)
    print(f"Test: {set_1}, {set_2} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

# is subset
set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
exp_res = True
test(set_1, set_2, exp_res)

# is not subset
set_1 = {1, 2}
set_2 = {3, 4, 5}
exp_res = False
test(set_1, set_2, exp_res)