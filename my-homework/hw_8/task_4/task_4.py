import json

FILE_PATH = "students.json"

def display_student_averages(file_path):

    try:
        with open(file_path, 'r') as file:
            students_data = json.load(file)

        students_averages = {}

        for student_key, student in students_data.items():
            student_name = f"{student['Name']} {student['Surname']}"
            grade = student['Grade']
            students_averages[student_name] = grade

        group_average = sum(students_averages.values()) / len(students_averages)

        print("Average scores for a student:")
        for student_name, average_score in students_averages.items():
            print(f"{student_name}: {average_score:.2f}")

        print("\nAverage score for the group:")
        print(f"{group_average:.2f}")
    except FileNotFoundError as error_msg:
        print(f"File not found. Error: {error_msg}")
    except json.JSONDecodeError as error_msg:
        print(f"Error decoding JSON: {error_msg}")
    except Exception as error_msg:
        print(f"Unexpected error: {error_msg}")

display_student_averages(FILE_PATH)