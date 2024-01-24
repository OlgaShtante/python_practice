import pickle
import numpy as np

FILE_PATH = 'matrix.pkl'
def display_matrix_determinant(file_path):
    try:
        with open(file_path, 'rb') as file:
            matrix = pickle.load(file)

        if len(matrix) != len(matrix[0]):
            print("Error: The matrix is not square.")
            return

        determinant = np.linalg.det(matrix)
        print(f"Determinant is {determinant} of matrix {matrix}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except pickle.UnpicklingError:
        print("Unable to unpickle the file.")
    except Exception as error_msg:
        print(f"{error_msg}")


display_matrix_determinant(FILE_PATH)