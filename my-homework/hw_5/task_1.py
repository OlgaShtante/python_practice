# define constants to make magic numbers clear:)
PHONE_LENGTH = 11
COUNTRY_CODE = '+375'

# create a function that format number from 11 digits to +375 (xx) xxxxxxx format
def format_phone_number(number):
    # check only 11 digits are allowed
    if not number.isdigit() or len(number) != PHONE_LENGTH:
        print("Некорректный ввод. Введите 11 цифр.")
    if number[0] == '8':
        # add replacement option to work for phone codes with duplicated digits, e.g., 044, 033
        if number[2] == number[3]:
            replacement_option = number[3] * 2
        else:
            replacement_option = number[3]

        # get formatted number
        formatted_number = number.replace(replacement_option, f"{replacement_option}) ", 1).replace(number[1], ' (',
                                                                                                    1).replace(
            number[0], COUNTRY_CODE, 1)
        return formatted_number
    else:
        print("Номер должен начинаться с 8.")

# get phone number
phone_number = str(input("Введите номер телефона: "))

number = format_phone_number(phone_number)

print(f"Отформатированный номер: {number}")
print("Отформатированный номер: %s" % number)
print("Отформатированный номер: {}".format(number))


# add tests
def test(number, exp_res):
    act_res = format_phone_number(number)
    assert act_res == exp_res, f"Error! Actual result: {act_res} does not match expected result: {exp_res}"

# (017)
test('80172567844', '+375 (17) 2567844')

# (029)
test('80295646422', '+375 (29) 5646422')

# (044)
test('80447892323', '+375 (44) 7892323')

# (033)
test('80336794546', '+375 (33) 6794546')
