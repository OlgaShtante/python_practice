# create a function to count words in sentences using enumerate
def count_words_in_sentences(input_text):
    sentences = [sentence.strip() for sentence in input_text.split('.') if sentence]
    sentence_lengths = [len(sentence.split()) for sentence in sentences]

    for i, length in enumerate(sentence_lengths, start=1):
        print(f"Sentence {i} has {length} words.")

# input text and see the result
input_text = "Python is an easy to learn language. It has many applications in various fields. You can use it for web development, data analysis, machine learning, and more."
count_words_in_sentences(input_text)

























