def szukajWLiscie(lista,a):
    count = 0
    for i in lista:
        if i == a:
            count += 1
    print(count)
szukajWLiscie([2,3,6,8,2,1,2],2)
szukajWLiscie([8,8,1,8,8],8)