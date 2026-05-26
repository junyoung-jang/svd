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
# deflection method have 2 methods but to represent svd using Hotelling's deflation method is efficient


def hotelingDeflation(matrix, eigenvalue, eigenvector):
    after_deflation = matrix - eigenvalue * np.outer(eigenvector, eigenvector)
    return powerMethod(after_deflation, 100)  
# Call powerMethod on the deflated matrix

def iterationhotelingDeflation(matrix, iterations):
    eigenvalues = []
    eigenvectors = []
    eigenvalue, eigenvector = powerMethod(matrix, 100)
    print("Eigenvalue:", eigenvalue)
    print("Eigenvector:", eigenvector)

    for i in range(1, iterations):  
        eigenvalue, eigenvector = hotelingDeflation(matrix, eigenvalue, eigenvector)
        print(f"Eigenvalue {i}:", eigenvalue)
        print(f"Eigenvector {i}:", eigenvector)
        eigenvalues.append(eigenvalue)
        eigenvectors.append(eigenvector)

    return eigenvalues, eigenvectors



