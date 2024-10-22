x = int(input("Podaj bok trójkąta: "))
string = "X"
for i in reversed(range(1,x+1)):
    print(" "*i,string)
    string += "X"