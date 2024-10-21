list = []
for i in range(2,100):
    check = 0
    for j in range(1,i+1):
        if(i%j==0):
            check += 1
    if check == 2:
        list.append(i)
list2 = []
for i in range(len(list)):
    for j in range(len(list)):
        if(list[j]-list[i]==2):
            list2.append([list[i],list[j]])
print(list2)


    
