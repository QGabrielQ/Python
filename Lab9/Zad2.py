lista = []
for i in range(10):
    x = int(input(f"Podaj liczbę {i}: "))
    lista.append(x)
max = lista[0]
for j in lista:
    if j > max:
        max = j
print(max)
