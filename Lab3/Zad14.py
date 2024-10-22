x = int(input("Podaj x: "))
x_str = str(x)
Liczby = []
if(x<10):
    Liczby.append(x%10)
    print(Liczby)
else:
    Liczby.append(x%10)
    perc = 10
    for i in range(0,len(x_str)-1):
        Liczby.append((x-x%10)//perc % 10)
        perc = perc * 10
print(Liczby)
print(sum(Liczby))
