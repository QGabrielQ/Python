import math
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if(a == 0):
    if(b == 0):
        if(c == 0):
            print("Nieskończenie wiele rozwiązań")
        else:
            print("Brak rozwiązań")
    else:
        x0 = -c/b
        print("Miejsce zerowe to:",x0)
else:
    delta = pow(b,2) - (4 * a * c)
    if(delta < 0):
        print("brak rozwiazań")
    if(delta == 0):
        x0 = -b/(2*a)
        print("Jedno rozwiązanie",x0)
    if(delta > 0):
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        if(x1==x2):
            print("Jedno rozwiązanie (podwójne)",x1)
        else:
            print("Dwa rozwiązania",x1,x2)


