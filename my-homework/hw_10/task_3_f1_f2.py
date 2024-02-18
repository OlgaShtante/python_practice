from typing import Dict, Union

def upper_case(func):
    def wrapper():
        original_dict = func()
        updated_dict = {k: v for k, v in original_dict.items()}
        updated_dict.update({k.upper(): v.upper() if isinstance(v, str) else v for k, v in original_dict.items()})
        return updated_dict

    return wrapper

@upper_case
def f1() -> Dict[str, int]:
    original_dict = {'a': 1, 'b': 2}
    return original_dict

@upper_case
def f2() -> Dict[str, Union[str, int]]:
    return {'a': 'a', 'b': 'b'}

print(f1())
print(f2())

