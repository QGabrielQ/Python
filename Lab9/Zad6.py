def NieOptEuklides(a,b):
    while(a!=b):
        if(a>b):
            a-=b
        else:
            b-=a
    return a,b
def OptEuklides(a,b):
    while(b!=0):
        pom = b
        b = a%b
        a = pom
    return a
print(NieOptEuklides(12,18))
print(OptEuklides(12,18))
