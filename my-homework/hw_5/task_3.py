DELIMITER = "."

# create a function to count words in sentences and return info for every sentence in the text
def count_words_in_sentence(input_text):
    #remove last period from the text
    text = input_text.strip(DELIMITER)

    #check if there is more than 1 sentence
    if DELIMITER in text:
        sentences = text.split(DELIMITER)
    else:
        sentences = [text]
        if not text.isalpha():
            return "Input does not include any text."

    #add loop for text with a few sentences
    result = ''
    for sentence in sentences:
        number_of_words = len(sentence.strip(" ").split(" "))
        ending = "s"
        if number_of_words ==1: ending = ""
        if not sentence.isspace():
            sentence_info = f"Sentence {sentences.index(sentence)+1} has {number_of_words} word{ending}. "
        else:
            sentence_info = f"Sentence {sentences.index(sentence)+1} is missing. "
        result += sentence_info
    return result

# input text
input_text = str(input("Input text / Введите текст: "))
text_info = count_words_in_sentence(input_text)

print(f"{text_info }")
print("%s" % text_info)
print("{}".format(text_info))

# add tests
def test(text, exp_res):
    act_res = count_words_in_sentence(text)
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

# data from task
text = '''Python is an easy to learn language. It has many applications in various fields. You can use it for web development, data analysis, machine learning, and more.'''
exp_res = 'Sentence 1 has 7 words. Sentence 2 has 7 words. Sentence 3 has 13 words. '
test(text,exp_res)

# one sentence
text = 'sentence.'
exp_res = 'Sentence 1 has 1 word. '
test(text,exp_res)

# period
text = "."
exp_res = "Input does not include any text."
test(text,exp_res)

# space
text = " "
exp_res = "Input does not include any text."
test(text,exp_res)