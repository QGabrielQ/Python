def bubblesort_max(Lista):
    for i in range(len(Lista)-1):
        for j in range(len(Lista)-i-1):
            if Lista[j] > Lista[j+1]:
                temp = Lista[j]
                Lista[j] = Lista[j+1]
                Lista[j+1] = temp
def bubblesort_min(Lista):
    for i in range(len(Lista)-1):
        for j in range(len(Lista)-i-1):
            if Lista[j] < Lista[j+1]:
                temp = Lista[j]
                Lista[j] = Lista[j+1]
                Lista[j+1] = temp

Lista=[6,2,7,1,5]
bubblesort_max(Lista)
print(Lista)
bubblesort_min(Lista)
print(Lista)
