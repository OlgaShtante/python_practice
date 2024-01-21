# get plural form for English word
def make_plural_form(word):
    exceptions = ['s', 'x', 'z', 'ch', 'sh']
    irregular_plurals = {'foot': 'feet', 'goose': 'geese', 'deer': 'deer', 'moose': 'moose'}

    # check if the word is in the irregular plurals
    if word in irregular_plurals:
        return irregular_plurals[word]

    # check if the word includes "man"
    if 'man' in word:
        return f"Pluralization not supported for words containing 'man'."

    if word.endswith(tuple(exceptions)):
        plural_form = f"{word}es"
    elif word.endswith('y') and len(word) > 1 and word[-2] not in 'aeiou':
        plural_form = f"{word[:-1]}ies"
    else:
        plural_form = f"{word}s"

    return plural_form

# input word, call the function and print the result
input_word = input("Enter an English word: ")
plural_form = make_plural_form(input_word)
print(plural_form)

# TBD
# function can be extended including more exceptions
#irregular_plurals = {
    #'child': 'children',
    #'man': 'men',
    #'woman': 'women',
    #'tooth': 'teeth',
    #'foot': 'feet',
    #'goose': 'geese',
    #'mouse': 'mice',
    #'deer': 'deer',
    #'moose': 'moose',
    #'person': 'people',
    # 'cactus': 'cacti',
    #'focus': 'foci',
    #'fungus': 'fungi',
    #'radius': 'radii',
    #'datum': 'data',
    #'analysis': 'analyses',
    #'criterion': 'criteria',
    #'phenomenon': 'phenomena',
#}

#for singular, plural in irregular_plurals.items():
    #print(f'{singular} - {plural}')

#list of words with only singular form
#Furniture
#Information
#Luggage
#Baggage
#Knowledge
#Advice
#Homework
#News
#Software
#Research

#list of words with only plural form
#Scissors
#Pants
#Glasses (when referring to eyeglasses)
#Trousers
#Pajamas
#Shorts
#Binoculars
#Tweezers
#Shears
#Belongings