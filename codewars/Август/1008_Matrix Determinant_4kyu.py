def minor(array):
    if len(array) == 1:
        return array[0][0]
    return array[0][0] * array[1][1] - array[1][0] * array[0][1]

def determinant_my(array):
    if len(array[0]) > 2:
        result = 0
        for i in range(len(array[0])):
            new_arr = []
            for j in range(len(array[0])):
                if j != i:
                    new_arr.append([array[j][k] for k in range(1, len(array[0]))])
            result += determinant_my(new_arr) * array[i][0] * (-1 + 2 * ((i + 1) % 2))
        return result
    else:
        return minor(array)


def determinant(matrix):
    #your code here
    result = 0
    l = len(matrix)

    #base case when length of matrix is 1
    if l == 1:
        return matrix[0][0]

    #base case when length of matrix is 2
    if l == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    #for length of matrix > 2
    for j in range(0, l):
        # create a sub matrix to find the determinant
        if l!=2:
            sub_matrix = []               
            sub_matrix = [(row[0:j]+row[j+1:]) for row in matrix[1:]]
        result = result + (-1)**j * matrix[0][j] * determinant(sub_matrix)
    return result

import numpy as np

def determinant(a):
    return round(np.linalg.det(np.matrix(a)))
print(determinant([[9,4,2,0],[3,1,1,2],[1,2,5,2],[11,3,0,9]]))
            
        