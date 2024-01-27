def power(x: float, y: int) -> float:
    if y == 0:
        return 1.0
    else:
        return x * power(x, y - 1)


try:
    x = float(input("Input number to power it: "))
    y = int(input("Input power: "))
    result = power(x, y)
    print(int(result) if result.is_integer() else result)

except ValueError as value_error:
    print(f"Input error: {value_error}. Input a number (float/int)")
except RecursionError as recur_error:
    print(f"Power error: {recur_error}. Input an integer")
except Exception as error_msg:
    print(f"Error: {error_msg}")


def test(n, p, exp_res):
    act_res = power(n,p)
    act_res == exp_res, f"Number {n} is a power of {p} does not match expected result {exp_res}"

n = 2
p = 2
exp_res = 4
test(n, p, exp_res)

n = -3
p = 3
exp_res = -27
test(n, p, exp_res)

n = 4
p = 0
exp_res = 1
test(n, p, exp_res)