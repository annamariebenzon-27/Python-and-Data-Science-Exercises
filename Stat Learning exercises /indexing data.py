import numpy as np
A=np.array(np.arange(16)).reshape((4,4))
print('producing a 2D array or 4x4 matrix \n', A)

#retrieve element of A
B=A[1,2]
print('To retrieve an element [row, column]:\n', B)
#to select rows
C= A[[1,3]]
print('Retriving rows:\n',C)
