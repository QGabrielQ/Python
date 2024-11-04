x = int(input('Podaj dodatnią liczbę naturalną: '))
i = 1
pierwsze = []
while i < x:
  check = 0
  for j in range(1,i+1):
    if(i%j==0):
      check += 1
  if check == 2:
    pierwsze.append(i)
  i += 1
print(pierwsze)
print(len(pierwsze))
      
