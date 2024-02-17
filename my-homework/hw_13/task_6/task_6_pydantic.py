from pydantic import BaseModel, ValidationError, field_validator

class StudentDTO(BaseModel):
    first_name: str
    last_name: str
    age: int
    course: int
    average_score: float

    @field_validator('first_name', 'last_name')
    def name_must_start_with_upper(cls, values):
        if not values[0].isupper():
            raise ValueError("Names must begin with a capital letter")
        return values

    @field_validator('age')
    def age_must_be_valid(cls, values):
        if not (18 <= values <= 30):
            raise ValueError("Age must be between 18 and 30")
        return values

    @field_validator('course')
    def course_must_be_valid(cls, values):
        if not (1 <= values <= 6):
            raise ValueError("Course must be between 1 and 6")
        return values

    @field_validator('average_score')
    def average_score_must_be_valid(cls, values):
        if not (1 <= values <= 100):
            raise ValueError("Average score must be between 1 and 100")
        return values
