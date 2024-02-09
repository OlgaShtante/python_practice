def sort_by_length(lst: list) -> list:
    return sorted(lst, key=len)


def test (test_data, exp_res):
    act_res = sort_by_length(test_data)
    print(act_res)
    act_res == exp_res, f"Error: data {test_data} is not sorted to {exp_res}"


# happy path
test_data = ["apple", "banana", "cherry", "date"]
exp_res = ['date', 'apple', 'banana', 'cherry']
test(test_data, exp_res)

test_data = [(0,), "", {"a":1, "b":2}, {1,2,3,4}, [9,8,7]]
exp_res = ['', (0,), {'a': 1, 'b': 2}, [9, 8, 7], {1, 2, 3, 4}]
test(test_data, exp_res)


# handled type errors
test_data = [1, 0.5, True, None]
for value in test_data:
    try:
        print(sort_by_length(value))
    except TypeError as type_error:
        print(f"Incorrect input. Error: {type_error}."
            f"\nEnsure insert object is iterable. ")
