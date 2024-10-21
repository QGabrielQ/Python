lista = []
for a in range(1,51):
    for b in range(1,51):
        for c in range(1,51):
            if(pow(a,2) + pow(b,2) == pow(c,2)):
                lista.append([a,b,c])
list2 = []
for i in lista:
    i.sort()
    list2.append(tuple(i))
list2 = set(list2)
list2 = list(list2)
list3 = []
for i in list2:
    list3.append(list(i))
print(list3)
