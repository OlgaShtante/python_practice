DELIMITER = ","
MSG ="Введите через запятую название книги, имя и фамилию автора, год издания"
ERROR_MSG = f"Некорректный ввод. {MSG}."
TITLE_ERROR_MSG = "Убедитесь, что внесли название книги."
AUTHOR_ERROR_MSG = "Убедитесь, что внесли имя и фамилию автора через пробел."
YEAR_ERROR_MSG = "Убедитесь, что год введен корректно (4 цифры), например, 2024"

# create function to format book info in 3 diff ways
def format_book_info(book_info):
    # check that input info is valid
    book_info = book_info.strip(DELIMITER)
    book_info_components = book_info.split(DELIMITER)
    if not DELIMITER in book_info or len(book_info_components) != 3:
        return ERROR_MSG
    book_title = book_info_components[0].strip(" ")
    if book_title.isspace() or book_title=="":
        return f"{ERROR_MSG} {TITLE_ERROR_MSG}"
    author = book_info_components[1].strip(" ")
    author_name = author.split()[0].title()
    author_surname = author.split()[-1].title()
    if len(author.split(" "))!= 2:
        return f"{ERROR_MSG} {AUTHOR_ERROR_MSG}"
    publish_year = book_info_components[2].strip(" ")
    if not (publish_year.isdigit() and len(publish_year)==4):
        return f"{ERROR_MSG} {YEAR_ERROR_MSG}"

    formatted_info_fstring = f"{author_surname}, {author_name}. {book_title}. {publish_year}."
    formatted_info_percent = "%s, %s. %s. %s." % (author_surname, author_name, book_title, publish_year)
    formatted_info_format = "{}, {}. {}. {}.".format(author_surname, author_name, book_title, publish_year)
    return formatted_info_fstring, formatted_info_percent, formatted_info_format

# input book info and call function to get formatted info
book_info = input(str(f"{MSG}: "))
formatted_book_info = format_book_info(book_info)
for book_info in formatted_book_info:
    print(book_info)

# add tests
def test(book_info, exp_res):
    act_res = format_book_info(book_info)
    if act_res and len(act_res)==3:
        assert act_res[0] == exp_res, f"Error: actual result: {act_res[0]} does not match expected result: {exp_res}"
        assert act_res[1] == exp_res, f"Error: actual result: {act_res[1]} does not match expected result: {exp_res}"
        assert act_res[2] == exp_res, f"Error: actual result: {act_res[2]} does not match expected result: {exp_res}"
    else:
        assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

# valid data
valid_data = "Война и мир, Лев Толстой, 1869"
formatted_data = "Толстой, Лев. Война и мир. 1869."
test(valid_data, formatted_data)


# invalid data - missing delimiter
invalid_data = "Book. author_name surname 1976"
test(invalid_data, ERROR_MSG)

# invalid data - missing argument
invalid_data = "  , author_name author_surname, 2000"
exp_res = f"{ERROR_MSG} {TITLE_ERROR_MSG}"
test(invalid_data, exp_res)

# invalid data - incorrect author name
invalid_data = "title, author, 2024"
exp_res = f"{ERROR_MSG} {AUTHOR_ERROR_MSG}"
test(invalid_data, exp_res)

# invalid data - incorrect year
invalid_data = "title, author_name author_surname, 69"
exp_res = f"{ERROR_MSG} {YEAR_ERROR_MSG}"
test(invalid_data, exp_res)



