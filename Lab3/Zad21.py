liczba_b = int(input("Początkowa liczba bakterii: "))
wzrost = float(input("Wzrost w każdym cyklu: "))
cykle = int(input("Liczba cykli: "))
for i in range(cykle):
    liczba_b = liczba_b * (1 + (wzrost/100))
    print("Godzina",i+1,":" ,int(liczba_b),"bakterii")