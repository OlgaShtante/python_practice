from math import *

# input of numbers
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

# calculation in 3 steps
# 1. calculate the 1st fraction
# 1.1 calculate numerator of the 1st fraction (the magnitude of the difference)
numerator_fraction_1 = abs(a - b)
# 1.2 calculate denominator of the 1st fraction (sum of b and c)
denominator_fraction_1 = b + c
# 1.3 calculate fraction 1
fraction_1 = numerator_fraction_1 /denominator_fraction_1

# 2. calculate the 2nd fraction
# 2.1 calculate numerator of the 2nd fraction
numerator_fraction_2 = pow(a, 2) + pow(b, 2) - c
# 2.2 calculate denominator of the 2nd fraction (square root of sum)
denominator_fraction_2 = 2 * sqrt(b + c)
# 2.3. calculate fraction 2
fraction_2 = numerator_fraction_2 / denominator_fraction_2

# 3. calculate the result
result = fraction_1 * fraction_2 * 3

# print the result
print(f"Результат вычисления выражения: {result:.4f}")