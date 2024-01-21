ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_LENGTH = 26

# create a function to encrypt message with Caesar cipher
def encrypt_message_with_caesar_cipher(original_message, step):
    encrypted_message = ''

    for char in original_message:
        if char.isalpha():
            # find the indexes of chars
            char_index = ALPHABET.index(char.upper()) #A=0-Z=25
            encrypted_index = (char_index + step) % ALPHABET_LENGTH

            # encrypt char preserving the original case and store it in a new message
            encrypted_char = ALPHABET[encrypted_index]
            encrypted_char = encrypted_char if char.isupper() else encrypted_char.lower()
            encrypted_message += encrypted_char
        else:
            # non-alpha chars are not encrypted
            encrypted_message += char

    return encrypted_message

# create a function to decrypt message with Caesar's cipher
def decrypt_message_with_caesar_cipher(encrypted_message, step):
    decrypted_message = ''

    for char in encrypted_message:
        if char.isalpha():

            # find the indexes of chars
            char_index = ALPHABET.index(char.upper())
            decrypted_index = (char_index - step) % ALPHABET_LENGTH

            # decrypt char preserving the original case and store it in a new message
            decrypted_char = ALPHABET[decrypted_index]
            decrypted_char = decrypted_char if char.isupper() else decrypted_char.lower()
            decrypted_message += decrypted_char
        else:
            #  non-alpha chars are not decrypted
            decrypted_message += char

    return decrypted_message


# call functions and print the results
original_message = str(input("Input message to encrypt: "))
step = 2
encrypted_message = encrypt_message_with_caesar_cipher(original_message, step)
decrypted_message = decrypt_message_with_caesar_cipher(encrypted_message, step)
print(f"Your original message: {original_message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")

#add test
def test(message, exp_res, step):
    encrypted_message = encrypt_message_with_caesar_cipher(message, step)
    decrypted_message = decrypt_message_with_caesar_cipher(encrypted_message, step)
    assert encrypted_message == exp_res, f"Error: actual result {encrypted_message} does not match expected result{exp_res}"
    assert decrypted_message == message, f"Error: actual result {decrypted_message} does not match expected result{message}"

message = "HELLO WORLD"
test(message, 'KHOOR ZRUOG', 3)