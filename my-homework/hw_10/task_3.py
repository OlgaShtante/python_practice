from typing import Dict, Union, List

def uppercase(function):
    def wrapper():

        original_dict = function()
        print(original_dict)

        def process_dict(dictionary):
            new_dict = {}
            for key, value in dictionary.items():
                upper_key = key.upper()
                print(upper_key)

                if isinstance(value, dict):
                    new_dict[upper_key] = process_dict(value)
                    print(new_dict[upper_key])
                elif isinstance(value, list):
                    new_dict[upper_key] = [process_dict(item) if isinstance(item, dict) else item for item in value]
                    print(new_dict[upper_key])
                else:
                    new_value = value.upper() if isinstance(value, str or int) else value
                    print(new_value)
                    new_dict[key] = value
                    print(new_dict[key])
                    new_dict[upper_key] = new_value
                    print(new_dict[upper_key])

            return new_dict

        processed_dict = process_dict(original_dict)
        print(processed_dict)

        for key, value in original_dict.items():
            if isinstance(value, dict):
                processed_dict[key] = value
                print(processed_dict[key])
        print(processed_dict)
        return processed_dict

    return wrapper


@uppercase
def f1() -> Dict[str, int]:
    return {'a': 1, 'b': 2}
print(f1())
#
# @uppercase
# def f2() -> Dict[str, Union[str, int]]:
#     return {'a': 'a', 'b': 'b'}
# print(f2())
#
# @uppercase
# def f3() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
#     return {'a': 'a', 'c': [{'b': 'b'}]}
# print(f3())
#
# @uppercase
# def f4() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
#     return {'a': 'a', 'c': [{'b': 1}, {'d': 2}]}
# print(f4())
#
#
#
