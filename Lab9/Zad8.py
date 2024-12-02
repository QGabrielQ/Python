def permutation(lst):
 if len(lst) == 0:
   return []
 if len(lst) == 1:
   return [lst]
 perms = [] 
 for i in range(len(lst)):
  m = lst[i]
  remLst = lst[:i] + lst[i+1:]
  for p in permutation(remLst):
   perms.append([m] + p)
 return perms
print(permutation(['A', 'B', 'C']))
#C len(lst) == 0 gdy lista jest pusta zwraca 0, len(lst) == 1 gdy lista ma jeden element zwracamy tę lista jako jedną permutacje
#D Przechowuje wszytkie permutacje
#E m - element listy wybierany do permutacji , remLst lista pozostałych elemntów po usunięciu m z lst
#F lst = ['A', 'B', 'C', 'D'] ,    i = 2 ,    m = 'C',  remLst = ['A', 'B', 'D']
#G Pętla iteruje po wszytkich permutacjach pozosotałych elementów remLst po usunięciu m
#G [m] + p dodaje element m na początek