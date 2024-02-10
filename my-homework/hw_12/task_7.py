from typing import List

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.courses: List[str] = []

class Course:
    def __init__(self, title: str, instructor: str):
        self.title = title
        self.instructor = instructor
        self.students: List[Student] = []

    def enroll(self, student: Student) -> None:
        self.students.append(student)
        student.courses.append(self.title)


if __name__ == "__main__":
    student1 = Student("Harry", 20)
    student2 = Student("Ron", 22)

    course = Course("Python Programming", "Pr. Snake")
    course.enroll(student1)
    course.enroll(student2)

    print(f"\nCourses taken by {student1.name}: {student1.courses[0]}")
    print(f"Courses taken by {student2.name}: {student2.courses[0]}")

