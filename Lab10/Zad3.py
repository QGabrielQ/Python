file= "/home/gabriel/Programming/Python/Lab10/liczby.txt"
f = open(file,"w")
for i in range(1,101):
    f.write(str(i)+'\n')
f.close()
f = open(file,"r")
print(f.read())
f.close()
Read = open(file,"r")
Update = []
for i in range(1,101):
    x = int(Read.readline())
    print(x)
    if(x%2==0):
        x += 10
        Update.append(x)
    else:
        Update.append(x)
Read.close()
Overwrite = open(file,"w")
for i in range(len(Update)):
    Overwrite.write(str(Update[i]) + "\n")
Overwrite.close()
Read = open(file,"r")
print(Read.read())
Read.close()


