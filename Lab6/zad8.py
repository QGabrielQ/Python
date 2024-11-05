def szukajWLiscie(lista,a):
    count = 0
    for i in lista:
        if i == a:
            count += 1
    return count
x= szukajWLiscie([1,2,5,3,5],5)
print(x)