results = []
def permute(a,l,r):
    if l == r:
        results.append(a)
    else:
        for i in range(l,r+1):
            a[l],a[i] + a[i],a[l]
            permute(a, l+1 , r)
            a[l],a[i] = a[i],a[l]
a = ['A','B','C']
permute(a,0,len(a)-1)
print(results)