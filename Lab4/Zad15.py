from random import seed
from random import randint
seed(123)
n = 7
m = 7
a = []
for i in range(n):
    a.append([0]*m)
    for j in range(m):
        x = randint(0,20)
        a[i][j] = x
    print(a[i])
    print(sum(a[i][(i+1):7]))
suma_nad_przekątną = 0
for i in range(len(a)):
    suma_nad_przekątną += sum(a[i][(i+1):7])
print(suma_nad_przekątną)