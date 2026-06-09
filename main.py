import numpy as np
from matrix_product import matrixProduct
import Eigenvalue_powermethod as ep

a = np.arange(0,12, 1)
a.shape = (3, 4)
at = a.T

### matrix product

aat = matrixProduct(a, at)

print(aat)

# eigenvalues, eigenvectors = ep.hotellingDeflation(aat, 2)

testvalue, testvector = ep.powerMethod(aat, 100)
print(testvalue)
print(testvector)



## Test the deflation method
eigenvalues, eigenvectors = ep.hotellingDeflation(aat, 3)
print("Deflation method eigenvalues:", eigenvalues)
print("Deflation method eigenvectors:", eigenvectors)   


## validation with numpy's built in function
eigenvalues, eigenvectors = np.linalg.eig(aat)
print("Numpy's eigenvalues:", eigenvalues)
print("Numpy's eigenvectors:", eigenvectors)   




