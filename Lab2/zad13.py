a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if(c<b):
    if(c < a):
        if(b<a):
            print("Liczby są ułożone rosnąco")
    else:
        print("Liczby nie są ułożone rosnąco")
else:
    print("liczby nie są ułożone rosnąco")