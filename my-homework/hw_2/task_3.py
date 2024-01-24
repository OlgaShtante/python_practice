# input integers
dividend = int(input("Введите целое число (делимое): "))
divisor = int(input("Введите целое число (делитель): "))

# note about numbers:
# rational <- real numbers -> irrational (pi)
#  |
# integers (include all whole numbers and their negative counterpart)
#  |
# whole numbers (all natural numbers including 0)
#  |
# natural numbers (positive whole numbers from 1)

# true division (result is a real number)
true_division_result = dividend / divisor

# divide by an integer (result is a natural number)
floor_division_result = dividend // divisor

# modules division (result is an integer)
remainder_result = dividend % divisor

# reverse operations to check division results:
check_of_true_division_result = true_division_result * divisor
check_of_floor_division_result = floor_division_result * divisor + remainder_result

# print the results to terminal
print(f"Частное полного деления {dividend} на {divisor}: {true_division_result}")
print(f"Целая часть деления {dividend} на {divisor}: {floor_division_result}")
print(f"Остаток от деления {dividend} на {divisor}: {remainder_result}")
print(f"Обратная операция полного деления: {true_division_result} * {divisor} = {check_of_true_division_result}")
print(f"Обратная операция деления с остатком: {floor_division_result} * {divisor} + {remainder_result} = {check_of_floor_division_result}")

