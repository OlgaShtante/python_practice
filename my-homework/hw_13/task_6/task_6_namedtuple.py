from collections import namedtuple

class StudentDTO(namedtuple('StudentDTO', ['first_name', 'last_name', 'age', 'course', 'average_score'])):
    def __new__(cls, first_name, last_name, age, course, average_score):
        instance = super().__new__(cls, first_name, last_name, age, course, average_score)
        instance._validate_fields()
        return instance

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