x = int(input("Podaj x: "))
Liczby = []
Liczby.append(x%10)
Liczby.append((x-x%10)//10 % 10)
Liczby.append((x-x%10)//100 % 10)
Liczby.append(((x-x%10)//1000 % 10))
print(sum(Liczby))
