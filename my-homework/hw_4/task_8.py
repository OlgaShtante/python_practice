# create a function to check if password is strong
import re
def check_password_complexity(password):
    weak_pass_msg ="Пароль не надежный"
    # check the length
    if len(password) < 8:
        return weak_pass_msg
    # check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return weak_pass_msg
    # check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return weak_pass_msg
    # check for at least one digit
    if not any(char.isdigit() for char in password):
        return weak_pass_msg
    # check for at least one special char from the set (!%@#$^&)
    if not any(char in "!%@#$^&" for char in password):
        return weak_pass_msg
    # check for allowed chars
    if not re.match("^[A-Za-z0-9!%@#$^&]+$", password):
        return weak_pass_msg
    # if all checks pass, the password is considered reliable
    return "Пароль надежный"

password = str(input("Bведите пароль для проверки надежности: "))
print(f"Результат проверки пароля: {check_password_complexity(password)}")