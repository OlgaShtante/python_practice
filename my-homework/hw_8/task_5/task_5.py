import json

DICT_1 = "dict_1.json"
DICT_2 = "dict_2.json"
def compare_json_files(file_1, file_2):
    try:
        with open(file_1, 'r') as dictionary_1, open(file_2, 'r') as dictionary_2:
            data_1 = json.load(dictionary_1)
            data_2 = json.load(dictionary_2)

        keys_1 = set(data_1.keys())
        keys_2 = set(data_2.keys())

        different_keys = keys_1.symmetric_difference(keys_2)
        common_keys = keys_1.intersection(keys_2)

        differences = []

        for key in common_keys:
            if data_1[key] != data_2[key]:
                differences.append(f"Key {key} is different. {DICT_1}: {data_1[key]}, {DICT_2}: {data_2[key]}")

        missing_keys_file_1 = different_keys - keys_2
        missing_keys_file_2 = different_keys - keys_1

        for missing_key in missing_keys_file_1:
            differences.append(f"Key {missing_key} is missing in {DICT_1}.")

        for missing_key in missing_keys_file_2:
            differences.append(f"Key {missing_key} is missing in {DICT_2}.")

        if differences:
            for difference in differences:
                print(difference)
        else:
            print("Files are identical.")

    except FileNotFoundError as error_msg:
        print(f"Error: {error_msg}")

compare_json_files(DICT_1, DICT_2)