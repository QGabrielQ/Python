def factorize(n,pierwsze=[]):
    if len(pierwsze)<1:
     for i in range(2,n):
      check = 0
      for j in range(1,i+1):
        if(i%j==0):
            check += 1
      if check == 2:
        pierwsze.append(i)
    while(n>1):
      for i in pierwsze:
        if(n%i==0):
          print(i," ",end="",)
          return factorize(n/i)
      
print(factorize(42069))

    
            

