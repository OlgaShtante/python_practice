def generate_subsets(input_set):
    n = len(input_set)
    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(list(input_set)[j])
        yield set(subset)


def test(test_data, exp_res):
    act_res = []
    for subset in generate_subsets(test_data):
        if subset ==set():
            subset = {}
        act_res.append(subset)
    assert act_res == exp_res, f"Actual result {act_res} does not match {exp_res}"
    print(act_res)

test_data = {1, 2, 3}
exp_res = [{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
test(test_data, exp_res)


#note
#https://stackoverflow.com/questions/53464944/what-does-ifcounter-1-j-0-do

