def binary(n,napis=""):
    if n == 1:
        napis = napis + str(n)
    else:
        napis = napis + str(n%2)
        n = n//2
        return binary(n,napis)
    print(napis[::-1])
print(binary(4))