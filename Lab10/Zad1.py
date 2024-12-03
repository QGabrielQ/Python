import time
from random import seed
from random import randint
def bubblesort_max(Lista):
    for i in range(len(Lista)-1):
        for j in range(len(Lista)-i-1):
            if Lista[j] > Lista[j+1]:
                temp = Lista[j]
                Lista[j] = Lista[j+1]
                Lista[j+1] = temp

seed(123)
Lista = []
for i in range(10000):
   x = randint(0,10000)
   Lista.append(x)

start = time.time()
bubblesort_max(Lista)
end = time.time()
print(end-start)
#a) 0.0004177093505859375
#b) 0.06832551956176758
#c) 18.85757064819336
 