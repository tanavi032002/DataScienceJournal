import csv

def read_matrix(filename):
    """Reads a matrix from a specified CSV file."""
    matrix = []
    try:
        with open(filename, "r", encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                matrix.append(list(map(int, row)))  # Convert each row to a list of integers
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: Ensure all matrix elements are integers.")
    return matrix

def multiply_matrices(matrix1, matrix2):
    """Multiplies two matrices."""
    if not matrix1 or not matrix2 or len(matrix1[0]) != len(matrix2):
        print("Error: Incompatible matrix sizes for multiplication.")
        return []
    
    result_rows, result_cols = len(matrix1), len(matrix2[0])
    result = [[0] * result_cols for _ in range(result_rows)]  # Initialize result matrix

    for i in range(result_rows):  # Iterate over rows of matrix1
        for j in range(result_cols):  # Iterate over columns of matrix2
            for k in range(len(matrix2)):  # Iterate over the elements
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # Perform multiplication
    return result

def write_matrix(matrix, filename):
    """Writes the specified matrix to a CSV file."""
    try:
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(matrix)  # Write all rows at once
    except Exception as e:
        print(f"Error: Could not write to file '{filename}'. {e}")

# File paths for input and output matrices
matrix1_path = 'matrix1.csv'  # Update with your file path as needed
matrix2_path = 'matrix2.csv'  # Update with your file path as needed
result_path = 'result_matrix.csv'

# Read matrices from the specified CSV files
matrix1 = read_matrix(matrix1_path)
matrix2 = read_matrix(matrix2_path)

# Check if matrices were read successfully before multiplying
if matrix1 and matrix2:
    # Multiply the matrices
    result_matrix = multiply_matrices(matrix1, matrix2)

    # Write the result to a new CSV file
    write_matrix(result_matrix, result_path)
    print(f"Resulting Matrix saved in '{result_path}'")

    # Read and print the resulting matrix from the CSV file
    result_matrix = read_matrix(result_path)
    print("Resulting Matrix:", result_matrix)
else:
    print("Matrix multiplication could not be performed due to read errors.")
