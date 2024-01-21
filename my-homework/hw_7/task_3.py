def is_list(input_list):
    if not isinstance(input_list, list):
        print("Input value is not a list")
        return False
    return True

def is_empty(input_value, value_type):
    if len(input_value)==0:
        print(f"{value_type} is empty")
        return True
    return False

def is_value_str(list_of_str):
    for string in list_of_str:
        if not isinstance(string, str):
            return False
    return True

def find_longest_shortest_words(list_of_words):

    if is_list(list_of_words):
        if not is_empty(list_of_words, 'List'):
            if is_value_str(list_of_words):

                longest_word = shortest_word = list_of_words[0]
                if len(list_of_words) == 1:
                    print(f"List include only one word {list_of_words[0]}")
                    return (list_of_words[0], list_of_words[0])
                else:
                    for word in list_of_words:
                        if sum(1 for _ in word) > sum(1 for _ in longest_word):
                            longest_word = word
                        elif sum(1 for _ in word) < sum(1 for _ in shortest_word):
                            shortest_word = word

                            result_tuple = longest_word, shortest_word
                            print(f"Longest and shortest words are {result_tuple}")
                            return result_tuple
        else:
            print("List does not include only strings")

def test(test_data, exp_res):
    act_res = find_longest_shortest_words(test_data)
    print(f"Test: {test_data} returns {act_res}")
    assert act_res == exp_res, f"Error: actual result: {act_res} does not match expected result: {exp_res}"

if __name__ == "__main__": #to avoid test execution when import function
    # valid data
    test_data = ["apple", "banana", "kiwi", "orange", "grape"]
    exp_res = ('banana', 'kiwi')
    test(test_data, exp_res)

    # list len 1
    test_data = ["test"]
    exp_res = ("test", "test")
    test(test_data, exp_res)

    # empty list
    test_data = []
    exp_res = None
    test(test_data, exp_res)

    # not only str
    test_data = ["word", 4.15, 1, (7,), {1, 2}, [0], {"id":1}, True, None]
    test(test_data, exp_res)
