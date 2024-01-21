from task_7 import is_list_of_integers

def is_sorted_asc(list):
    is_sorted = all(list[i] <= list[i + 1] for i in range(len(list) - 1))
    return is_sorted

def merge_sorted_arrays(arr1, arr2):
    if not (is_list_of_integers(arr1) and is_list_of_integers(arr2)):
        print("One of arrays is invalid")
        return []

    if not (is_sorted_asc(arr1) and is_sorted_asc(arr2)):
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)

    merged_array = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])

    return merged_array

def test(array1, array2, exp_res):
    act_res = merge_sorted_arrays(array1, array2)
    print(f"Test: {array1, array2} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

array1 = [1, 3]
array2 = [2, 4]
exp_res = [1, 2, 3, 4]
test(array1, array2, exp_res)

array1 = [5, 3, 1]
array2 = [9, 0, -12]
exp_res = [-12, 0, 1, 3, 5, 9]
test(array1, array2, exp_res)

array1 = [0]
array2 = []
exp_res = [0]
test(array1, array2, exp_res)

array1 = "string"
array2 = ["A"]
exp_res = []
test(array1, array2, exp_res)