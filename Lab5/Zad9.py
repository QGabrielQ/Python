x = int(input("Podaj liczbe: "))
x1 = x
suma = 0
while (x>0):
    suma += x %10
    x //= 10
print(f"Suma cyfr liczby {x1} wynosi",suma)
