import numpy as np
A = np.array([[1,2,3],[4,5,6]])
print(A)
At = np.transpose(A)
print(At)
A = [[2,1,4],
     [0,1,1]]
B = [[6,3,-1,0],
     [1,1,0,4],
     [-2,5,0,2]]
C = np.matmul(A,B)
print(C)