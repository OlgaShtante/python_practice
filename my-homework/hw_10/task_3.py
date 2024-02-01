from typing import Dict, Union, List

def uppercase(function):
    def wrapper():

        original_dict = function()

        def process_dict(dictionary):
            new_dict = {}
            for key, value in dictionary.items():
                upper_key = key.upper()

                if isinstance(value, dict):
                    new_dict[upper_key] = process_dict(value)
                elif isinstance(value, list):
                    new_dict[upper_key] = [process_dict(item) if isinstance(item, dict) else item for item in value]
                else:
                    new_value = value.upper() if isinstance(value, str or int) else value
                    new_dict[key] = value
                    new_dict[upper_key] = new_value

            return new_dict

        processed_dict = process_dict(original_dict)

        for key, value in original_dict.items():
            if isinstance(value, dict):
                processed_dict[key] = value

        return processed_dict

    return wrapper


@uppercase
def f1() -> Dict[str, int]:
    return {'a': 1, 'b': 2}
print(f1())

@uppercase
def f2() -> Dict[str, Union[str, int]]:
    return {'a': 'a', 'b': 'b'}
print(f2())

@uppercase
def f3() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 'b'}]}
print(f3())

@uppercase
def f4() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 1}, {'d': 2}]}
print(f4())



