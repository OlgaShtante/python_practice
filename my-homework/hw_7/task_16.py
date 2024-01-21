def get_missing_letters_set(input_string):
    start_char = "a"
    start_char_unicode_point = ord(start_char) #65
    end_char = "z"
    end_char_unicode_point = ord(end_char) #122

    alphabet_set = set(map(lambda i: chr(i), range(start_char_unicode_point, end_char_unicode_point + 1)))
    new_set = alphabet_set - set(input_string.lower())
    missing_letters_set = set(sorted(new_set))

    if len(missing_letters_set) == 0:
        print(f"String '{input_string}' includes all letters of English alphabet.")
        return None

    print("Letters not included in the string:", missing_letters_set)
    return missing_letters_set

user_input = str(input("Input a string: "))
get_missing_letters_set(user_input)

def test(test_data, exp_res):
    act_res = get_missing_letters_set(test_data)
    print(f"Test: {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

# return set
test_data = "Hello, world!"
exp_res =  {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 's', 't', 'u',
'v', 'x', 'y', 'z'}
test(test_data, exp_res)

# return None
test_data = "The quick brown fox jumps over the lazy dog"
exp_res = None
test(test_data, exp_res)
