MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': ' ',
}
# create a function to convert morse into message
def convert_morse_to_text(morse_code):
    allowed_chars = '.- '
    cleaned_morse_code = ''.join(char for char in morse_code if char in allowed_chars)
    print(cleaned_morse_code)
    morse_words = cleaned_morse_code.split(' ')
    print(morse_words)

    text_message = ''
    for morse_word in morse_words:
        if morse_word in MORSE.values():
            text_message += [char for char, code in MORSE.items() if code == morse_word][0]
        elif morse_word == '':
            text_message += ' '

    return text_message

# input code, call the function and print the result
input_morse_code = str(input("Input morse code to convert into text: "))
original_text = convert_morse_to_text(input_morse_code)
# test_data_from_task = '..A. -&. Fw --l- -* ---.---- A --. --AT 3. 8--- 7-- '
print(original_text)

