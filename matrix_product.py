import numpy as np

def matrixProduct(matrix1, matrix2):
    m, a1 = matrix1.shape
    a2, n = matrix2.shape

    if a1 != a2:
        raise ValueError(
             print("Cannot do matrix product. please check matrixs dimension")
        )


    matrix2_transpose = matrix2.T

    mn = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            mn[i, j] = np.sum(matrix1[i,:] * matrix2_transpose[j,:])

    return mn
