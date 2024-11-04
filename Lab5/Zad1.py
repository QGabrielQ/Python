
 # macierz zerowa
A = [[1,2,3],[4,5,6]]
n = len(A)
At = [[0]*(n) for i in range(n+1)]  
print(At)
for i in range(len(A)):
    for j in range(len(A)+1):
        At[j][i] = A[i][j]
print(At)