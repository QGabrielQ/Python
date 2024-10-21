a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if(a == b == c):
    print("a,b,c są równe")
if(a == b != c):
    print("a i b są równe")
if(a == c != b):
    print("a i c są równe")
if(b == c != a):
    print("b i c są równe")
if(a != b != c):
    print("Nie ma pary liczb równych")