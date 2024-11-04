liczba = int(input("Podaj liczbę dodatnią: "))
suma = 0 
i = 1
liczby = [i]
while sum(liczby) <= liczba:
    i += 1
    liczby.append(i)
liczby.pop()
wynik = "Liczba pierwszych dodatnich liczb naturalnych, których suma jest niewiększa niż {} wynosi {}"
wynik = wynik.format(liczba,len(liczby))
print(liczby)
print(wynik)