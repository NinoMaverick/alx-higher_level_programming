#!/usr/bin/python3

def square_matrix_simple(matrix):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through each row in the matrix
    for row in matrix:
        # Create a new row to store squared values
        squared_row = []
        # Iterate through each element in the row
        for num in row:
            # Square the element and append to the new row
            squared_row.append(num ** 2)
        # Append the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix
