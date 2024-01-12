DELIMITER = " "
ERROR_MSG = "Некорректный ввод. Введите минимум два слова с пробелом между ними."
# create a function to revert words order in the phrase
def reverse_words_order(input_phrase):
    #remove extra whitespace
    input_phrase = input_phrase.strip(DELIMITER)
    if not DELIMITER in input_phrase:
        return ERROR_MSG
    else:
        words_list = input_phrase.split(DELIMITER)
        return " ".join(list(reversed(words_list)))
# get a phrase
input_phrase = str(input("Введите фразу или несколько случайных слов через пробел: "))

# get result and print it with 3 diff formatting types
result = reverse_words_order(input_phrase)

print(f"{result}")
print("%s" % result)
print("{}".format(result))


# TBD: nothing was mentioned about the capital letters.
# e.g., only the first word in the phrase started with the capital letter.
# should this letter become lowercase when the word is moved at the end and vice versa?
# should a new word at the first position start with a capital letter?

# add tests
def test(phrase, exp_res):
    act_res = reverse_words_order(phrase)
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"
# " "
test(" ", ERROR_MSG)

# one word
test(" one_word ", ERROR_MSG)

# two words
test("two words", "words two")

# three words
test(" three_words to test", "test to three_words")