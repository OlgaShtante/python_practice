import requests
import time
from typing import Callable

def retry(attempts: int, delayed: bool):
    def decorator(function: Callable[..., requests.Response]) -> Callable[..., requests.Response]:
        def wrapper(*args, **kwargs) -> requests.Response:
            for attempt in range(1, attempts + 1):
                try:
                    response = function(*args, **kwargs)
                    print(f"Attempt {attempt}:\nStatus Code: {response.status_code};\nError: {response.raise_for_status()}\n")
                    return response
                except requests.RequestException as error_msg:
                    print(f"Attempt {attempt}: {error_msg}")
                    if attempt < attempts:
                        if delayed:
                            time.sleep(attempt * 2 + 3)
                        else:
                            time.sleep(0)
                    else:
                        raise error_msg
        return wrapper
    return decorator


@retry(attempts=3, delayed =True)
def get_python() -> requests.Response:
    return requests.get('https://python.org', timeout=0.05)

response = get_python()

@retry(attempts=3, delayed=False)
def get_python2() -> requests.Response:
    return requests.get('https://python.org', timeout=0.05)

response = get_python2()