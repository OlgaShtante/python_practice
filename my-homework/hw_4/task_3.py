# create a function to check if year is leap/non-leap
def is_leap_year(year):
    # check if the year is within a valid range
    if not (1 <= year <= 2024):
        return "Введено неверное значение! Введите год от 1 до 2024."
    if 1 <= year <= 2024:
        # check if the year is a leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return "Високосный"
        else:
            return "Не високосный"

# get a year to check
inserted_year = int(input("Введите год, чтобы узнать, является ли он високосным: "))

# call the function and check the year
result = is_leap_year(inserted_year)

# display the result
print(result)