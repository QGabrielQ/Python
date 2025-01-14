napis = str(input("Podaj napis: ")).lower() #sedes
lenght = len(napis)

if(lenght%2 == 0):
    hlenght = lenght/2
else:
    hlenght = (lenght)//2
j = lenght - 1
same_letter_count = 0
for i in range(hlenght):
    if(napis[i]==napis[j]):
        same_letter_count += 1
    j -= 1
if(same_letter_count == hlenght):
    print("Napis jest palindromem!")
else:
    print("Napis nie jest palindromem!")
napisList = list(napis)
print(napisList)