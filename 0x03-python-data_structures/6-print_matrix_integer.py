#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    string = ""
    for row in matrix:
        for col in row:
            string += "{:d}".format(col)
            if col != row[-1]:
                string += " "
        if matrix[len(matrix) - 1] != row:
            string += '\n'
    print(string)
