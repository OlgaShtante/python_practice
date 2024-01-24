# input 4-digit number
number = int(input("Введите четырехзначное число: "))

# check that the input number has only 4 digits
if 1000 <= number <= 9999:
    # find reversed number
    reversed_number = (number % 10) * 1000 + ((number // 10) % 10) * 100 + ((number // 100) % 10) * 10 + (number // 1000)
    # calculate difference between original and reverted number
    difference = number - reversed_number

    # print the result to terminal
    print(f"Оригинальное число: {number}")
    print(f"Число, записанное задом наперед: {reversed_number}")
    print(f"Разность между оригинальным и обратным числами: {difference}")
else:
    # print error message if the input is not 4-digit number
    print("Некорректное значение! Введите четырехзначное число.")