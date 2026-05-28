# Eigenvalue Power method

import numpy as np
from matrix_product import matrixProduct
def powerMethod(matrix, iterations):
    a = np.random.rand(matrix.shape[0], 1)
    for i in range(iterations):
        a = matrixProduct(matrix, a)
        a = a / np.linalg.norm(a)
        
    eigenvector = a
    eigenvalue = np.dot(eigenvector.T, np.dot(matrix, eigenvector))[0, 0]
    return eigenvalue, eigenvector


# Deflation method to find the next eigenvalue and eigenvector
# deflection method have 2 methods but to represent svd using Hotelling's deflation method is efficient



# Call powerMethod on the deflated matrix

def hotellingDeflation(matrix, iterations):
    eigenvalues = []
    eigenvectors = []

    for i in range(0, iterations):  
        eigenvalue, eigenvector = powerMethod(matrix, 100)
        eigenvalues.append(eigenvalue)
        eigenvectors.append(eigenvector)
        print(f"Eigenvalue {i}:", eigenvalue)
        print(f"Eigenvector {i}:", eigenvector)
        after_deflation = matrix - eigenvalue * np.outer(eigenvector, eigenvector)
        eigenvalue, eigenvector = powerMethod(after_deflation, 100)
        matrix = after_deflation

    return eigenvalues, eigenvectors



