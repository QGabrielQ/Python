macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#POD PRZEKĄTNĄ
#[\ 2 3]
#[4 \ 6] - 4 + 7 + 8 = 19
#[7 8 \]
Rozmiar = len(macierz) #Rozmiar = 3
suma = 0
print("POD PRZEKĄTNĄ \n   0 1 2 \n   | | | \n0-[\ 2 3] \n1-[4 \ 6] \n2-[7 8 \]")
for i in range(Rozmiar): 
    print("Iteracja ",i+1," dla i: ",i)
    for j in range(i): 
        print("Iteracja ",j+1," dla j: ",j)
        print("Suma przed: ",suma)
        suma += macierz[i][j]
        print("Element ","[",i,"]","[",j,"]", " Wartość: ",macierz[i][j])
        print("Suma po: ",suma) 
    print("\n")
print("Wynik: ",suma)
print("\n")
#NAD PRZEKĄTNĄ
#[\ 2 3]
#[4 \ 6] - 2 + 3 + 6 = 11
#[7 8 \]
Rozmiar = len(macierz)
suma = 0
print("NAD PRZEKĄTNĄ \n   0 1 2 \n   | | | \n0-[\ 2 3] \n1-[4 \ 6] \n2-[7 8 \]")
for i in range(Rozmiar):
    print("Iteracja ",i+1," dla i: ",i)
    for j in range(i+1,Rozmiar):
        print("Iteracja ",j," dla j: ",j)
        print("Suma przed: ",suma)
        suma += macierz[i][j]
        print("Element ","[",i,"]","[",j,"]", " Wartość: ",macierz[i][j])
        print("Suma po: ",suma) 
    print("\n")
print("Wynik: ",suma)
#POD PRZEKĄTNĄ
#[1 2 /]
#[4 / 6] - 6 + 8 + 9 = 23
#[/ 8 9]
Rozmiar = len(macierz)
suma = 0
print("POD PRZEKĄTNĄ \n   0 1 2 \n   | | | \n0-[1 2 /] \n1-[4 / 6] \n2-[/ 8 9]")
for i in range(Rozmiar):
    print("Iteracja ",i+1," dla i: ",i)
    for j in range(Rozmiar):
        print("Iteracja ",j+1," dla j: ",j)
        if i > Rozmiar - 1 - j:
         print("Suma przed: ",suma)
         suma += macierz[i][j]
         print("Element ","[",i,"]","[",j,"]", " Wartość: ",macierz[i][j])
         print("Suma po: ",suma) 
        else:
         print("Warunek i > Rozmiar - 1 -j nie spełniony.")
    print("\n")
print("Wynik: ",suma)
#NAD PRZEKĄTNĄ
#[1 2 /]
#[4 / 6] - 1 + 2 + 4 = 7
#[/ 8 9]
Rozmiar = len(macierz)
suma = 0
print("NAD PRZEKĄTNĄ \n   0 1 2 \n   | | | \n0-[1 2 /] \n1-[4 / 6] \n2-[/ 8 9]")
for i in range(Rozmiar):
    print("Iteracja ",i+1," dla i: ",i)
    for j in range(Rozmiar):
        print("Iteracja ",j+1," dla j: ",j)
        if i < Rozmiar - 1 - j:
         print("Suma przed: ",suma)
         suma += macierz[i][j]
         print("Element ","[",i,"]","[",j,"]", " Wartość: ",macierz[i][j])
         print("Suma po: ",suma) 
        else:
           print("Warunek i < Rozmiar - 1 - j nie spełniony.")
    print("\n")
print("Wynik: ",suma)