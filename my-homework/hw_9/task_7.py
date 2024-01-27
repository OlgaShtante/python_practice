from typing import List, Callable

def modify_list(lst: List[int], *funcs: Callable[[int], int]) -> None:
    for i in range(len(lst)):
        for func in funcs:
            lst[i] = func(lst[i])

def is_prime(number: int) -> bool: #last condition
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


test_data = [1, 2, 3]
modify_list(test_data, lambda x: x + 1, lambda x: x * 2)
print(test_data) #[4, 6, 8]
test_data = [0, 1, -2]
modify_list(test_data,lambda x: x**2 if x % 2 == 0 else x)
print(test_data) #[0, 1, 4]
test_data = [-3, 3, 2]
modify_list(test_data,lambda x: x + 1 if x % 2 != 0 else x)
print(test_data) # [-2, 4, 2]
test_data = [10, 0, 3]
modify_list(test_data,lambda x: x * 3 if is_prime(x) else x)
print(test_data) #[10, 0, 9]

