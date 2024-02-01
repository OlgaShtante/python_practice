from typing import List
import time

def benchmark(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 4)
        print(f"Spent Time: {elapsed_time:.4f} seconds")
        return result

    return wrapper

def slicer(function):
    def wrapper(sequence: List[int]) -> List[int]:
        if len(sequence) > 10:
            raise ValueError("Input list length must be 10 or less.")
        result = function(sequence)
        print(f"Original Sequence: {sequence}")
        print(f"Modified Sequence: {result}")
        return result

    return wrapper

@benchmark
@slicer
def calculate_factorial(sequence: List[int]) -> List[int]:
    new_sequence = [1]
    for i in range(1, len(sequence)):
        new_sequence.append(new_sequence[-1] * i)

    return new_sequence

test_data = [1,2,3,4,5,6,7,8,9,10]
actual_result = calculate_factorial(test_data)

