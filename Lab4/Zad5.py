Imiona_str = str(input("Podaj parę imion: "))
Imiona_split = Imiona_str.split(",")
for i in Imiona_split:
    lenght = len(i)
    if(i[lenght-1]=="a"):
        print(i)