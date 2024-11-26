def factorize(n,flist=[]):
  if n == 1:
    return flist
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      flist.append(i)
      print(i)
      return factorize(n//i,flist)
factorize(10)
