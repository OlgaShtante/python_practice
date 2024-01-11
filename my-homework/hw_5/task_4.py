book_info = str(input("Введите через запятую название книги, автора и год издания: "))

book_info_array = book_info.split(",")
if len(book_info_array)<3:
    print("Некорректный ввод. Ввведите данные книги в следующем формате: Название книги, имя и фамилия автора, год издания")

book_name = book_info_array[0]
author_name_array = book_info_array[1].split(" ")
if len(author_name_array)<2:
    print("Имя автора должно включать имя и фамилию")
year_of_publish = book_info_array[-1]

#add capital
print(f"{author_name_array[-1]}, {author_name_array[-2]}. {book_name}.{year_of_publish}.")