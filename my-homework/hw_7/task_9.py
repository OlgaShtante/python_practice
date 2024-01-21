def set_operations(set_1, set_2):
    union_set = set_1 | set_2
    intersection_set = set_1 & set_2
    diff_set = set_1 - set_2
    symmetric_diff_set = set_1 ^ set_2

    return union_set, intersection_set, diff_set, symmetric_diff_set
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference:", diff_set)
    print("Symmetric difference:", symmetric_diff_set)

try:
    set1 = eval(input("Input the 1st set, e.g., {1, 2}: "))
    set2 = eval(input("Input the 2nd set, e.g., {3, 4}: "))
    set_operations(set1, set2)

except Exception as error_msg:
    print(f"Invalid input. Error: {error_msg}")

def test(set_1, set_2, exp_res):
    act_res = set_operations(set_1, set_2)
    print(f"Test: {set_1}, {set_2} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

# valid data
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
exp_res = ({1, 2, 3, 4, 5, 6}, {3, 4}, {1, 2}, {1, 2, 5, 6})
test(set_1, set_2, exp_res)