from typing import Dict, Union, List

def uppercase(func):
    def wrapper():
        result = func()
        updated_result = {}

        for key, value in result.items():
            updated_key = key.upper()
            if isinstance(value, dict):
                updated_result= {k: v for k, v in result.items()}
                updated_result.update({k.upper(): v.upper() if isinstance(v, str) else v for k, v in result.items()})
            elif isinstance(value, list):
                updated_list = []
                for item in value:
                    updated_item = {}
                    for k, v in item.items():
                        updated_item[k] = v
                        updated_item[k.upper()] = v if isinstance(v, int) else v.upper()
                    updated_list.append(updated_item)
                updated_result[key] = updated_list
                updated_result[updated_key] = updated_list
            else:
                updated_result[key] = value
                updated_result[updated_key] = value.upper() if isinstance(value, str) else value

        return updated_result

    return wrapper

@uppercase
def f1() -> Dict[str, int]:
    return {'a': 1, 'b': 2}

@uppercase
def f2() -> Dict[str, Union[str, int]]:
    return {'a': 'a', 'b': 'b'}

@uppercase
def f3() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 'b'}]}

@uppercase
def f4() -> Dict[str, Union[str, int, List[Dict[str, int]]]]:
    return {'a': 'a', 'c': [{'b': 1}, {'d': 2}]}


print(f1())
print(f2())
print(f3())
print(f4())