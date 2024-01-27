from typing import List, Union

def count_sum_of_list_values(lst: List[Union[int, List]]) -> int:
    total_sum = 0
    for item in lst:
        if isinstance(item, list):
            total_sum += count_sum_of_list_values(item)
        elif isinstance(item, int):
            total_sum += item

    if total_sum == 0:
        raise ValueError("No numbers found in the list.")

    return total_sum


try:
    test_data_1 = [1, [2, 3, [4, 5]], 6]
    test_data_2 = []
    test_data_list = [test_data_1 , test_data_2]
    for test_data in test_data_list:
        result = count_sum_of_list_values(test_data)
        print(result)
except ValueError as error_msg:
    print(f"Error: {error_msg}")