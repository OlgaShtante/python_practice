# input text
text = str(input('Введите текст: '))

# remove last period to simplify split
if text[-1]==".":
    text = text.rstrip(text[-1])


#print(len(text.split(".")))

#"Sentence 1 has 7 words. Sentence 2 has 7 words.
#Sentence 3 has 13 words.". Программа должна использовать 3 метода форматирования (fstrings, % и format) вывести 3 отформатированные строки.

