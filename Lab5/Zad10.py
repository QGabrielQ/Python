Bits = []
x = int(input("Podaj liczbe:"))
while x>0:
  bit = x%2
  x = x//2
  Bits.append(bit)
Bits.reverse()
print(Bits)