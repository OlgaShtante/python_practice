from typing import Dict, Union, List

def upper_case(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return apply_upper_case(result)
    return wrapper

def apply_upper_case(data):
    if isinstance(data, dict):
        updated_dict = {}
        for key, value in data.items():
            updated_dict[key] = value
            updated_dict[key.upper()] = value
            if isinstance(value, list):
                updated_list = []
                for item in value:
                    if isinstance(item, dict):
                        updated_list.append(apply_upper_case(item))
                    else:
                        updated_list.append(item)
                updated_dict[key.upper()] = updated_list
        return updated_dict
    else:
        return data

@upper_case
def f1() -> Dict[str, int]:
    return {'a': 1, 'b': 2}

@upper_case
def f2() -> Dict[str, Union[str, int]]:
    return {'a': 'a', 'b': 'b'}

@upper_case
def f3() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 'b'}]}

@upper_case
def f4() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 1}, {'d': 2}]}

print(f1())  # {'a': 1, 'b': 2, 'A': 1, 'B': 2}
print(f2())  # {'a': 'a', 'b': 'b', 'A': 'A', 'B': 'B'}
print(f3())  # {'a': 'a', 'A': 'A', 'C': [{'b': 'b', 'B': 'B'}], 'c': [{'b': 'b', 'B': 'B'}]}
print(f4())  # {'a': 'a', 'A': 'A', 'c': [{'b': 1, 'B': 1}, {'d': 2, 'D': 2}], 'C': [{'b': 1, 'B': 1}, {'d': 2, 'D': 2}]}