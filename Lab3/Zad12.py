list = [0,23,54,31,57,243,67,35,3726,623262]
max = list[0]
min = list[0]
for i in list:
    if(i > max):
        max = i
    if(i < min):
        min = i
print(min,max)