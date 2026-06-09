import numpy as np
from matrix_product import matrixProduct
import Eigenvalue_powermethod as ep
from PIL import Image

# below is the test code for the power method and deflation method, you can uncomment it to run the test.
'''
a = np.array([[1,4,7, 10], [2,8,5, 13]])
at = a.T


### matrix product

aat = matrixProduct(a, at)

print(aat)

# eigenvalues, eigenvectors = ep.hotellingDeflation(aat, 2)

testvalue, testvector = ep.powerMethod(aat, 100)
print(testvalue)
print(testvector)



## Test the deflation method
eigenvalues, eigenvectors = ep.hotellingDeflation(aat, 2)
print("Deflation method eigenvalues:", eigenvalues)
print("Deflation method eigenvectors:", eigenvectors)   


## validation with numpy's built in function
eigenvalues, eigenvectors = np.linalg.eig(aat)
print("Numpy's eigenvalues:", eigenvalues)
print("Numpy's eigenvectors:", eigenvectors)   
'''

# Let reconstruct arbitrary image using SVD and power method





