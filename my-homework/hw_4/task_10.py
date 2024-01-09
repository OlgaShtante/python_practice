import re
def check_password_complexity(password):
    weak_pass_msg = "Пароль не надежный"
    # check the length
    if len(password) < 8:
        return weak_pass_msg
    # check for a combination of uppercase, lowercase, digits, and special characters
    if not any(char.isupper() for char in password) or \
       not any(char.islower() for char in password) or \
       not any(char.isdigit() for char in password) or \
       not any(char in "!%@#$^&" for char in password):
        return weak_pass_msg
    # check for allowed chars
    if not re.match("^[A-Za-z0-9!%@#$^&]+$", password):
        return weak_pass_msg
    #if all checks pass, the password is considered reliable
    return "Пароль надежный"

password = input("Введите пароль для проверки надежности: ")
print(f"Результат проверки пароля: {check_password_complexity(password)}")