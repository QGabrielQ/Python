
def wyszukaj(towar,nazwa):
   for product in towar:
      for y in product.values():
         if y == nazwa:
            print(print(product))

def sumuj(towar,nazwa):
   for product in towar:
      for y in product.values():
         if y == nazwa:
            print(product['ilosc']*product['cena'])

def sumuj_wszytko(towar):
   Suma = 0
   for product in towar:
    for y in product.values():
        Suma += product['ilosc']*product['cena']
   print(Suma)
def dodajtowar(towar,nazwa,jednostka,ilosc,cena):
   product = {}
   product.update({'nazwa':nazwa,'jednostka':jednostka,'ilosc':ilosc,'cena':cena})
   towar.append(product)
def aktualizuj_ilosc(towar,nazwa,ilosc):
   for product in towar:
      for y in product.values():
         if y == nazwa:
            product.update({'ilosc':ilosc})
def filtr_jednostka(towar,jednostka):
   for product in towar:
      for y in product.values():
         if y == jednostka:
            print(product)
   
            

   

def main():
 towar = [{'nazwa': 'banan', 'jednostka': 'kg', 'ilosc': 10, 'cena': 3},
 {'nazwa': 'jabłko', 'jednostka': 'kg', 'ilosc': 16, 'cena': 2.5},
 {'nazwa': 'mąka pszenna', 'jednostka': 'op.', 'ilosc': 30, 'cena': 2.5},
 {'nazwa': 'mydło', 'jednostka': 'szt.', 'ilosc': 6, 'cena': 1.5},
 {'nazwa': 'jogurt naturalny', 'jednostka': 'szt.', 'ilosc': 20, 'cena': 1.5},
 {'nazwa': 'papier toaletowy 8 rolek', 'jednostka': 'op.', 'ilosc': 10, 'cena': 9}]
 wyszukaj(towar,"banan")
 sumuj(towar,"jabłko")
 sumuj_wszytko(towar)
 dodajtowar(towar,'Orzeszki','szt.',30,4.50)
 print(towar)
 aktualizuj_ilosc(towar,'Orzeszki',5)
 print(towar)
 filtr_jednostka(towar,'kg')
 
if __name__ == "__main__":
    main()