# Eigenvalue Power method

import numpy as np
from matrix_product import matrixProduct
def powerMethod(matrix, iterations):
    a = np.ones(matrix.shape[0])
    for i in range(iterations):
        a = matrixProduct(matrix, a)
        eigenvector = a / np.linalg.norm(a)
        eigenvalue = np.dot(eigenvector, matrixProduct(matrix, eigenvector)) / np.dot(eigenvector, eigenvector)
    return eigenvalue, eigenvector


# Deflation method to find the next eigenvalue and eigenvector
# deflection method have 2 methods but




