# create a function to get title based on name and print message with the title
def get_greetings_with_title(name):
    last_letter_of_name = name[-1]
    match last_letter_of_name:
        case "\u0430" | "\u044F":  # "а" (u0430) and "я" (u044F) patterns work only with unicode
            title = "госпожа"
        case _:
            title = "господин"
    return f"Здравствуйте, {title} {name.title()}"

# get the last name from the full name
full_name = str(input("Введите имя и фамилию: "))
last_name = full_name.split(" ")[-1]

# call the function and show the message
message = get_greetings_with_title(last_name)
print(message)

# note:
# in the case of real form implementation and the necessity to work with first and last names separately, it is better to store them in different fields.