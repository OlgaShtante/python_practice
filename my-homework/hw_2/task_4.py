# input 3-digit number
number = int(input("Введите трехзначное число: "))

# check that the input number has only 3 digits
if 100 <= number <= 999:
    # separating a number into digits
    digit_1 = number // 100
    digit_2 = (number % 100) // 10
    digit_3 = number % 10
    # print digits to terminal if the input number has only 3 digits
    print(f"Число {number} состоит из цифр: {digit_1}, {digit_2}, {digit_3}")
else:
    # print error message if the input is not 3-digit number
    print("Некорректное значение! Введите трехзначное число.")