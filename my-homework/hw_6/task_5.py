from task_4 import is_matrix, is_list_includes_int
def transpose_list(matrix):
    if not is_matrix(matrix):
        print(f"Input data {matrix} is not a matrix")
        return []

    if not is_list_includes_int(matrix):
        print(f"Input data {matrix} includes not only integers")
        return []

    transposed_list = [list(row) for row in zip(*matrix)]
    return transposed_list

def test(test_data, exp_res):
    act_res = transpose_list(test_data)
    print(f"Test: {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

test_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
exp_res = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
test(test_data, exp_res)

test_data = [[0, 1], [1, 2], [2, 3]]
exp_res = [[0, 1, 2], [1, 2, 3]]
test(test_data, exp_res)

test_data = ['1', '2', '3']
exp_res = []
test(test_data, exp_res)
