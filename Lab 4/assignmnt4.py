def readNames(file_path):
    with open(file_path, 'r') as f:
        names = [line.strip() for line in f.readlines()]
    return names

def loadMatrix(names):
    matrix = [name for name in names]
    return matrix

def convertToColumnMajor(matrix):
    if not matrix:
        return []

    max_length = max(len(name) for name in matrix)
    column_major_matrix = ['' for _ in range(max_length)]

    for i in range(max_length):
        for name in matrix:
            if i < len(name):
                column_major_matrix[i] += name[i]
            else:
                column_major_matrix[i] += ' '

    # Trim trailing spaces from each column
    column_major_matrix = [column.rstrip() for column in column_major_matrix]

    return column_major_matrix

def calculateTotalCharacterLength(names):
    total_length = sum(len(name) for name in names)
    return total_length

def main():
    file_path = r'C:\Users\Tanavi\OneDrive\Desktop\JJJJJJJ\assignmnet4\names.txt'  # Updated file path
    output_file_path = 'output.txt'  # You can change this if needed

    names = readNames(file_path)
    print("Original Names:")
    print(names)
    
    matrix = loadMatrix(names)
    print("\nMatrix:")
    for row in matrix:
        print(row)
    
    column_major_matrix = convertToColumnMajor(matrix)
    print("\nColumn Major Matrix:")
    print(column_major_matrix)
    
    total_length = calculateTotalCharacterLength(names)
    print("\nTotal Length of All Names:")
    print(total_length)
    
    # Format column-major matrix as desired
    formatted_column_major = [f"'{column}'" for column in column_major_matrix]
    
    # Store column-major matrix in output file
    with open(output_file_path, 'w') as f:
        f.write("Column Major Matrix:\n")
        f.write(', '.join(formatted_column_major) + '\n')
        f.write("\nTotal Length of All Names:\n")
        f.write(str(total_length) + '\n')

    print(f"\nResults stored in {output_file_path}")

if __name__ == "__main__":
    main()
