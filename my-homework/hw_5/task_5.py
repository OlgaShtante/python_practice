import re

# get number
input_msg = "Введите число в двоичной системе исчисления"
number = str(input(f"{input_msg}: "))

# check number
if not re.match("[0-1]*$", number):
    print(f"Некорректный ввод. {input_msg}.")

# output should be
# Программа должна "Decimal: 42, Octal: 52, Hexadecimal: 2A."
# использовать 3 метода форматирования (f-strings, % и format) вывести 3 отформатированные
# строки.
