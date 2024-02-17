from typing import TypedDict

class StudentDTO(TypedDict):
    first_name: str
    last_name: str
    age: int
    course: int
    average_score: float

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._validate_fields()

    def _validate_fields(self):
        if not (self['first_name'].isalpha() and self['last_name'].isalpha() and
                self['first_name'][0].isupper() and self['last_name'][0].isupper()):
            raise ValueError("First and last names must consist only of letters of the English alphabet and begin with a capital letter")

        if not (18 <= self['age'] <= 30):
            raise ValueError("Age must be between 18 and 30")

        if not (1 <= self['course'] <= 6):
            raise ValueError("Course must be between 1 and 6")

        if not (1 <= self['average_score'] <= 100):
            raise ValueError("Average score must be between 1 and 100")