# create a function to generate a random password
import random
def generate_password(password_length):
    # default set of chars
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    # select chars randomly from the specified set
    password = ''.join(random.choice(chars) for _ in range(password_length))
    return password

# get desired length of the password and call the function
password_length = int(input("Введите желаемую длину пароля, например, от 8 до 20 символов: "))
print(f"Generated password: {generate_password(password_length)}")
