def silnia(n):
    silnia = 1
    if n == 1:
        return 1
    else:
        for i in range(n):
            silnia = silnia * n
            n -= 1
        return silnia
print(silnia(4))

        