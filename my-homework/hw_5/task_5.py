import re

# create a function to convert binary number into decimal, octal and hexadecimal numbers
def convert_binary_number(binary_number):
    results = ''
    # check that string includes only 0 and 1
    if not re.match("^[0-1]+$", binary_number):
        results = "Error"
    else:
        # convert binary to decimal
        dec_number= int(binary_number, 2)

        # convert decimal to octal
        oct_number = oct(dec_number)

        # convert decimal to hexadecimal
        hex_number= hex(dec_number)

        formatted_fstring = f'Decimal: {dec_number}, Octal: {oct_number}, Hexadecimal: {hex_number}.'
        formatted_percent = 'Decimal: %d, Octal: %s, Hexadecimal: %s.' % (dec_number, oct_number, hex_number)
        formatted_format= 'Decimal: {}, Octal: {}, Hexadecimal: {}.'.format( dec_number, oct_number, hex_number)
        results = formatted_fstring, formatted_percent, formatted_format

    return results

# input binary number and call the function
binary_number= str(input("Input binary number / Введите бинарное число: "))
results = convert_binary_number(binary_number)

# print results
if results == "Error":
    print(f"{results}: Incorrect input")
else:
    for result in results:
        print(result)

# add tests
def test(binary_number, exp_res):
    act_res = convert_binary_number(binary_number)
    if len(act_res) == 3:
        assert act_res[0] == exp_res, f"Error! Actual result {act_res[0]} does not match the expected result {exp_res}"
        assert act_res[1] == exp_res, f"Error! Actual result {act_res[1]} does not match the expected result {exp_res}"
        assert act_res[2] == exp_res, f"Error! Actual result {act_res[2]} does not match the expected result {exp_res}"
    else:
        assert act_res == exp_res, f"Error! Actual result {act_res} does not match the expected result {exp_res}"
# valid data
valid_data = '1010101'
exp_res = 'Decimal: 85, Octal: 0o125, Hexadecimal: 0x55.'
test(valid_data, exp_res)

# invalid data
invalid_data = '345'
exp_res = 'Error'
test(invalid_data, exp_res)
