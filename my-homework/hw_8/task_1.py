def sum_of_squares_generator(n):
    current_sum = 0
    for number in range(1, n + 1):
        current_sum += number**2
        print(f"Sum of squares of all numbers up to {number}: {current_sum}")
        yield current_sum

# check with 10
for result in sum_of_squares_generator(10):
    print(result)




