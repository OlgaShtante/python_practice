from typing import List

def factorial(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("List should include only positive integers; nested lists are not allowed.")

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def list_of_factorials(sequence: List[int]) -> List[int]:
    if len(sequence) > 10:
        raise ValueError("The sequence cannot have more than 10 items.")

    def calculate_factorials(number_list: List[int]) -> List[int]:
        return [factorial(num) for num in number_list]

    return calculate_factorials(sequence)

def slicer(function):
    def wrapper(sequence: List[int]) -> List[int]:
        result = []
        for i in range(0, len(sequence), 10):
            result.extend(function(sequence[i:i + 10]))
        return result

    return wrapper


@slicer
def list_of_factorials(sequence: List[int]) -> List[int]:
    if len(sequence) > 10:
        raise ValueError("The sequence cannot have more than 10 elements.")

    def calculate_factorials(number_list: List[int]) -> List[int]:
        return [factorial(num) for num in number_list]

    return calculate_factorials(sequence)

def calculate_sum_of_items(sequence:List[int]) -> int:
    result = sum(list_of_factorials(sequence))
    return result



def test(test_data, exp_res):
    act_res = calculate_sum_of_items(test_data)
    print(act_res)
    act_res == exp_res, f"Error: actual result {act_res} does not match expected result {exp_res}"



test_data = [0]
exp_res = 1
test(test_data, exp_res)

test_data = []
exp_res = 0
test(test_data, exp_res)


test_data = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
exp_res = 20
test(test_data, exp_res)