MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        'А': '.-', 'Б': '-...', 'В': '- --', 'Г': '--.',
        'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
        'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..',
        'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
        'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
        'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
        'Ш': '----', 'Щ': '--.-', 'Ъ': '-. -', 'Ы': '-.--',
        'Ь': '-..-', 'Э': '. -.', 'Ю': '..--', 'Я': '.-.-',
    }

def convert_text_to_morse(message):
    morse_message = ''
    for char in message.upper():
        if char.isalpha() or char in (' ', '.'):
            morse_message += MORSE.get(char, '') + ' '
        else:
            morse_message += ' '

    return morse_message.strip()

# input and call the function
message = str(input("Input message to convert to Morse: "))
result = convert_text_to_morse(message)

# print the result with 3 diff formatting
print(f'{result}')
print('%s' % result)
print('{}'.format(result))

# add test
def test(message, exp_res):
    act_res = convert_text_to_morse(message)
    assert act_res == exp_res, f"Error: actual result {act_res} does not match expected result {exp_res}"

test("privet", ".--. .-. .. ...- . -")