from random import seed
from random import randint
seed(123)
randomnumber = randint(0,100)
print("Wylosowano liczbe!")
x = 0
while (x <= randomnumber or x >= randomnumber):
    x = int(input("Podaj twoją odpowiedz: "))
    if (x < randomnumber):
        print("Liczba jest wieksza od podanej!")
        break
    if (x > randomnumber):
        print('liczba jest mniejsza od podanej')
        break
print(randomnumber)

