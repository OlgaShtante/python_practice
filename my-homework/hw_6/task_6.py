def build_matrix_from_keyboard():
    input_err = "Invalid input. Only integers are allowed."
    try:
        rows = int(input("Enter the number of rows: "))
    except ValueError:
        print(input_err)
        return []

    try:
        cols = int(input("Enter the number of columns: "))
    except ValueError:
        print(input_err)
        return []

    if(rows or cols) == 0:
        print("Incorrect input: rows and columns cannot be 0")
        return []

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element for row {i+1} column {j+1}: "))
            row.append(element)
        matrix.append(row)

    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

    return matrix


matrix = build_matrix_from_keyboard()
def sum_matrix_elements_by_cols(matrix):
    if matrix ==[]:
        print("Invalid matrix")
        return None
    else:
        col_sums = [sum(col) for col in zip(*matrix)]
        return col_sums

result = sum_matrix_elements_by_cols(matrix)
print("Sum of elements across columns:", result)


def test(test_data, exp_res):
    act_res = sum_matrix_elements_by_cols(test_data)
    print(f"Test: {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

test_data = [[0, 1], [2, 3]]
exp_res = [2, 4]
test(test_data, exp_res)

test_data = []
exp_res = None
test(test_data, exp_res)

