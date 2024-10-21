list = []
for i in range(2,100):
    check = 0
    for j in range(1,i+1):
        if(i%j==0):
            check += 1
    if check == 2:
        list.append(i)
print(list)
