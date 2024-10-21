a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if(a == b):
    if(b==c):
        print("Wszytkie są równe")
    if(b!=c):
        print("a i b są równe")
if(a == c):
    if(c==b):
        print("Wszytkie są równe")
    if(b!=c):
        print("a i c są równe")
if(c == b):
    if(a==c):
        print("Wszytkie są równe")
    if(b!=a):
        print("a i b są równe")
if(a!=b):
    if(c!=a):
        print("Nie ma równych liczb")