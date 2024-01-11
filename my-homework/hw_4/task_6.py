# create a function to calculate even numbers in the list
def sum_of_even_numbers(numbers):
    match numbers:
        case []:
            return 0
        case [first, *rest] if first % 2 == 0:
            return first + sum_of_even_numbers(rest)
        case [_ignore, *rest]:
            return sum_of_even_numbers(rest)


# input list of numbers and call the function
input_numbers = input("Введите список чисел, например, [1, 2, 3, 4, 5]: ")
if '[' in input_numbers and ']' in input_numbers:
    numbers_list = eval(input_numbers)
    print(f"Сумма четных чисел: {sum_of_even_numbers(numbers_list)}")
else:
    print("Некорректный ввод, смотрите пример: [1, 2, 3, 4, 5]")