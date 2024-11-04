x = int(input("Podaj liczbe: "))
liczby = []
if(x<10):
    print(x%10)
else:
    perc = 10
    liczby.append(x%10)
    x = x - x%10
    print(x)
    print(x - (x//perc))
    while x >= 0:
        liczby.append((x//perc)%10)
        x =- (x//perc)%10
        perc = perc * 10
        
print(liczby)