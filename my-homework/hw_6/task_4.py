def is_matrix(matrix):
    if not isinstance(matrix, list):
        return False

    if not all(isinstance(row, list) for row in matrix):
        return False

    num_columns = len(matrix[0]) if matrix else 0
    if not all(len(row) == num_columns for row in matrix):
        return False

    return True

def find_max_values(matrix):
    error_msg = f"Input data {matrix} is not a matrix"
    if not is_matrix(matrix):
        print(error_msg)
        return []

    result = []

    for row in matrix:
        int_values = [value for value in row if isinstance(value, int)]
        if int_values:
            result.append(max(int_values))
        else:
            result.append(None)

    return result


def test(test_data, exp_res):
    act_res = find_max_values(test_data)
    print(f"Test: {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"


test_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
exp_res = [3, 6, 9]
test(test_data, exp_res)

test_data = [[0, '1'], ['1', 2], ['2', '3']]
exp_res = [0, 2, None]
test(test_data, exp_res)

test_data = [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
exp_res = []
test(test_data, exp_res)

test_data = ([1, 2],[3, 4])
exp_res = []
test(test_data, exp_res)

test_data = 'string'
exp_res = []
test(test_data, exp_res)

test_data = None
exp_res = []
test(test_data, exp_res)
