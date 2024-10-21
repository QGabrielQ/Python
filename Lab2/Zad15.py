a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if(a + b > c and b + c > a and c + a > b):
    if(a==b==c):
        print("Trójkąt równoboczny , ostrokątny")
    elif(a==b or b == c or c == a):
        print("Trójkąt równoramienny")
        if(pow(a,2)+pow(b,2)<pow(c,2) or pow(b,2)+pow(c,2)<pow(a,2) or pow(c,2)+pow(a,2)<pow(b,2)):
            print(",rozwartokątny")
        elif(pow(a,2)+pow(b,2)==pow(c,2) or pow(b,2)+pow(c,2)==pow(a,2) or pow(c,2)+pow(a,2)==pow(b,2)):
            print(", prostokątny")
        else:
            print(",ostrokątny")
    else:
        print("trójkąt różnoboczny")
        if(pow(a,2)+pow(b,2)<pow(c,2) or pow(b,2)+pow(c,2)<pow(a,2) or pow(c,2)+pow(a,2)<pow(b,2)):
            print(", rozwartokątny")
        elif(pow(a,2)+pow(b,2)==pow(c,2) or pow(b,2)+pow(c,2)==pow(a,2) or pow(c,2)+pow(a,2)==pow(b,2)):
            print(", prostokątny")
        else:
            print("ostrokątny")
else:
    print("to nie sa boki trójkąta")