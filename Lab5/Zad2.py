A = [[2,1,4],
     [0,1,1]]
B = [[6,3,-1,0],
     [1,1,0,4],
     [-2,5,0,2]]
Awiersz = len(A)
Bkolumn = len(B[0])
C = [[0]*Bkolumn for i in range(Awiersz)]
for i in range(Awiersz):
    for j in range(Bkolumn):
        for k in range(Awiersz+1):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]
print(C)