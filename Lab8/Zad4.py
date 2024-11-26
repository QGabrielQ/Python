def RekSuma(n):
    if n == 1:
        return 1
    else:
        return RekSuma(n-1)+n
print(RekSuma(3))