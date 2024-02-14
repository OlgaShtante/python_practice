from dataclasses import dataclass

@dataclass
class StudentDTO:
    first_name: str
    last_name: str
    age: int
    course: int
    average_score: float

    def __post_init__(self):
        self._validate_fields()

    def _validate_fields(self):
        if not (self.first_name.isalpha() and self.last_name.isalpha() and
                self.first_name[0].isupper() and self.last_name[0].isupper()):
            raise ValueError("First and last names must consist only of letters of the English alphabet and begin with a capital letter")

        if not (18 <= self.age <= 30):
            raise ValueError("Age must be between 18 and 30")

        if not (1 <= self.course <= 6):
            raise ValueError("Course must be between 1 and 6")

        if not (1 <= self.average_score <= 100):
            raise ValueError("Average score must be between 1 and 100")

if __name__ == "__main__":
    try:
        student_1 = StudentDTO("John", "Doe", 16, 2, 100)
    except ValueError as error_msg:
        print(f"ValueError: {error_msg}")

    try:
        student_2 = StudentDTO("John", "Li", 18, 2, 101)
    except ValueError as error_msg:
        print(f"ValueError: {error_msg}")

    try:
        student_3 = StudentDTO("Jane", "Air", 18, 7, 98)
    except ValueError as error_msg:
        print(f"ValueError: {error_msg}")

    try:
        student_4 = StudentDTO("Jane", "Air", "18", 3, 100)
    except TypeError as error_msg:
        print(f"TypeError: {error_msg}")