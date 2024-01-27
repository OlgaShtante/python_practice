def reverse_helper(number: int) -> int or str: #use str to add missing zero
    def reverse_number(number_to_reverse, reversed_number):
        if number_to_reverse == 0:
            return reversed_number
        else:
            return reverse_number(number_to_reverse// 10, (reversed_number * 10) + number_to_reverse % 10)

    reversed_number = reverse_number(number, 0)

    def add_missing_zero(number_to_reverse: int, reversed_number: int) -> int or str:
        if len(str(number_to_reverse)) == len(str(reversed_number)):
            return reversed_number
        else:
            qty_of_missing_zero = len(str(number_to_reverse)) - len(str(reversed_number))
            zero = "0"
            return f"{zero * qty_of_missing_zero}{reversed_number}"

    return add_missing_zero(number, reversed_number)


def test(test_data, exp_res):
    try:
        act_res = reverse_helper(test_data)
        print(act_res, type(act_res))
        act_res == exp_res, f"Error: actual result {act_res} does not match expected {exp_res}"
    except Exception as error_msg:
        print(f"Error: {error_msg}")

test_data = 123456789
exp_res = 987654321
test(test_data, exp_res)

test_data = 768900000
exp_res = "000009867"
test(test_data, exp_res)
