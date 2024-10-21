a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if(a>b):
    if(b > c):
        print(c)
    else:
        print(b)
else:
    if(c < a):
        print(c)
    else:
        print(a)
