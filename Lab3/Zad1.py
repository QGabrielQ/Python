#tworzenie lsity
parzyste = [0,2,4,6,8,10]
print(parzyste)
parzyste.append(12)
print(parzyste)

#wyświetlenie pojedynczych elementów
print(parzyste[0])
print(parzyste[3])
print(parzyste[-2])

#wyswietlanie długosci 
print(len(parzyste))

#wyswietlenie wykrojonych fragmentów (slices)

print(parzyste[:])
print(parzyste[:3])
print(parzyste[6:3])
print(parzyste[-3:])
print(parzyste[:-3])
fragm = parzyste[1:-1]
print(fragm)