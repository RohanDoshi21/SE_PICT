# Author: Rohan Doshi
# Problem statement
"""
Write a Python program to compute following computation on matrix:
a) Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix
"""


class Matrix:
    def __init__(self):
        self.matrix = []
        self.rows = 0
        self.columns = 0
        self.acceptMatrix()

    def acceptMatrix(self):
        self.rows = int(input("Enter number of Rows: "))
        self.columns = int(input("Enter number of Columns: "))
        for i in range(self.rows):
            matrix = []
            for j in range(self.columns):
                matrix.append(int(input()))
            self.matrix.append(matrix)


def printMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end=" ")
        print()


def additionMatrix(matrix1, matrix2):
    if matrix1.rows != matrix2.rows or matrix1.columns != matrix2.columns:
        print("Matrices are not suitable for addition")
        return -1

    matrix3 = []
    for i in range(matrix1.rows):
        mat = []
        for j in range(matrix1.columns):
            x = matrix1.matrix[i][j] + matrix2.matrix[i][j]
            mat.append(x)
        matrix3.append(mat)

    return matrix3


def subtractionMatrix(matrix1, matrix2):
    if matrix1.rows != matrix2.rows or matrix1.columns != matrix2.columns:
        print("Matrices are not suitable for subtraction")
        return -1

    matrix3 = []
    for i in range(matrix1.rows):
        mat = []
        for j in range(matrix1.columns):
            x = matrix1.matrix[i][j] - matrix2.matrix[i][j]
            mat.append(x)
        matrix3.append(mat)

    return matrix3


def multiplicationMatrix(matrix1, matrix2):
    if matrix1.rows != matrix2.columns:
        print("Matrices are not suitable for multiplication")
        return -1

    matrix3 = []
    for i in range(matrix1.rows):
        mat = []
        for j in range(matrix2.columns):
            mat.append(0)
        matrix3.append(mat)

    for i in range(matrix1.rows):
        for j in range(matrix2.columns):
            for k in range(matrix2.rows):
                matrix3[i][j] += matrix1.matrix[i][k] * matrix2.matrix[k][j]

    return matrix3


print("Matrix 1")
m1 = Matrix()

print("Matrix 2")
m2 = Matrix()

print("*" * 10)
print("Matrix 1")
printMatrix(m1.matrix)
print('*' * 10)
print("Matrix 2")
printMatrix(m2.matrix)
print('*' * 10)

while (True):
    print("*"*10 + "Menu" + "*"*10)
    print("""1 . Matrix Addition
2. Matrix Subtraction
3. Matrix Multiplication
-1. EXIT """)
    choice = int(input("Enter number for the operation to be performed: "))
    if choice == 1:
        print('*' * 10)
        print("Addition")
        if (additionMatrix(m1,m2) != -1):
            printMatrix(additionMatrix(m1, m2))
        

    if choice == 2:
        print('*' * 10)
        print("Subtraction")
        if (subtractionMatrix(m1,m2) != -1):
            printMatrix(subtractionMatrix(m1, m2))
        

    if choice == 3:
        print('*' * 10)
        print("multiplication")
        if (multiplicationMatrix(m1,m2) != -1):
            printMatrix(multiplicationMatrix(m1, m2))
        

    if choice == -1:
        print("Exit")
        break
