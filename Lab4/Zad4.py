boki = str(input("Podaj boki prostokąta: "))
boki_split = boki.split(" ")
print(boki_split)
for i in range(len(boki_split)):
    boki_split[i] = int(boki_split[i])
print("Pole prostokąta to: ", boki_split[0]*boki_split[1], "Obwód to: ", boki_split[0]*2 + boki_split[1]*2)