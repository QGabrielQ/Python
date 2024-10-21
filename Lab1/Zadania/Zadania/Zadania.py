print("Zad1")
print("Hello World!")
print("\n")

print("Zad2")
print("   ^")
print("  ^^^")
print(" ^^^^^")
print("^^^^^^^")
print("  ^^^")
print(" ^^^^^")
print("^^^^^^^")
print("  ###")
print("\n")

print("Zad3")
x=7
print(x)
print("\n")
print("Zad4")
a = 7
b = 5
print(a)
print(a + 3)
print(a * 3)
print(a + b)
print(a / b)
print("Suma to a i b to: ", a + b)
print("a = ",a, ", b = ",b)
c = b - a
print(c)
print("\n")
print("zad5")
a = 4
b = 5
print("Liczba a = ",a,"; Liczba b = ",b)
c = pow(a, 2) + pow(b, 2)
print("Suma kwadratow tych liczb to: ", c)
print("\n")
print("Zad6")
a = 5
h = 3
Pole = (a*h)/2
print("Pole trójkąta o boku: ",a," i wysokości: ",3," Wynosi: ", Pole)
print("\n")
print("Zad7")
bok1 = 8
bok2 = 10
Pole = bok1*bok2
Obw = (2*bok1) + (2*bok2)
print("Pole prostokąta o bokach: ",bok1, " i ",bok2," to ",Pole, " a jego obwod to ",Obw)
print("\n")
print("Zad8")
znaki = "abc hej!"
print(znaki)
print("\n")
print("Zad9")
a = 3
print("Gdy do", a, "dodasz 1, to wyjdzie", a + 1)
print("Gdy do", a, "dodasz 1, to wyjdzie", a + 1, sep="")
print("Gdy do", a, "dodasz 1, to wyjdzie", a + 1, sep="-")
print("\n")
print("Zad10")
bombka = "o"
print("   ^")
print("  ^^^")
print(" ^",bombka,"^^^",sep="")
print("^^^^^^",bombka,"^",sep="")
print("  ^^^")
print(" ^^",bombka,"^^^",sep="")
print("^^^^^",bombka,"^^",sep="")
print("  ###")
print("\n")
print("Zad11")
import math
a =16
b = math.sqrt(a)
print(b)
print(math.pi)
print(math.sin(0))
print(math.sin(math.pi/2))
print(math.floor(2.3))
print("\n")
print("Zad12")
a = 4
Pole = pow(a,2)
Obw = a*4
Przekatna = a * math.sqrt(2)
print("Pole:",Pole, "Obw:",Obw,"Przekatna:", Przekatna)
print("\n")
print("Zad13")
wejscie = int(input("1 - stopnie -> radiany, 2 - radiany -> stopnie: "))
if(wejscie == 1):
    stopnie = int(input("Podaj stopnie: "))
    radiany =(stopnie*math.pi)/180
    print("Radiany: ",radiany)
if(wejscie == 2):
    radiany = int(input("Podaj radiany: "))
    stopnie = (radiany*180)/math.pi
    print("Stopnie: ",stopnie)

print("\n")
print("Zad14")
print("Podaj dwa boki a i b (Liczby dodatnie) oraz kat alfa (w zakresie 180)")
a = int(input("Bok a: "))
b = int(input("Bok b: "))
alfa = int(input("Kat alfa: " ))
alfa = (alfa * math.pi)/180
h = b * math.sin(alfa)
Pole = (a * h)/2
print("Bok a: ",a,"Bok b: ",b, "Wysokość h: ",h, "Kat alfa: ", alfa, "Pole: ",Pole)
print("\n")
print("Zad15")
x_a = int(input("Punkt A-x: "))
y_a = int(input("Punkt A-y: "))
x_b = int(input("Punkt B-x: "))
y_b = int(input("Punkt B-y: "))
x = x_b - x_a
x = pow(x,2)
y = y_b - y_a
y = pow(y, 2)
d = math.sqrt(x + y)
print("Odleglosc miedzy pkt. A i B wynosi: ",d)
