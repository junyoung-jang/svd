import numpy as np
from matrix_product import matrixProduct

a = np.arange(0,12, 1)
a.shape = (3, 4)
at = a.T

### matrix product

aat = matrixProduct(a, at)

print(aat)




