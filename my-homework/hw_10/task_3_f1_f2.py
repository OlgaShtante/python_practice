from typing import Dict, Union

def uppercase(func):
    def wrapper():
        original_dict = func()
        updated_dict = {k: v for k, v in original_dict.items()}
        updated_dict.update({k.upper(): v.upper() if isinstance(v, str) else v for k, v in original_dict.items()})
        return updated_dict

    return wrapper

@uppercase
def f1() -> Dict[str, int]:
    original_dict = {'a': 1, 'b': 2}
    return original_dict

@uppercase
def f2() -> Dict[str, Union[str, int]]:
    return {'a': 'a', 'b': 'b'}

print(f1())
print(f2())

