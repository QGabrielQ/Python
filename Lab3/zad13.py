x = int(input('Podaj x: '))
check = 0
if(x == 1):
   print("Jest liczba pierwszą")
else:
    for i in range(1,x+1):
      if(x%i==0):
        check += 1
    if(check == 2):
     print('Liczba jest pierwsza')
    else:
     print('Liczba nie jest pierwsza')

