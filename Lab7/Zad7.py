from collections import Counter
def find_max(dict):
    dictValues = list(dict.values())
    max = dictValues[0]
    for i in dictValues:
        if(i > max):
            max = i
    print(max)
def merge_dictionaries(dict1,dict2):
    dict3 = {**dict1,**dict2}
    print(dict3)
def odd_sum_dictionaries(dict1,dict2):
    D1Val = list(dict1.values())
    D2Val = list(dict2.values())
    sumD1Val = 0
    sumD2Val = 0
    for i in D1Val:
        if i%2 != 0:
            sumD1Val += i
    for i in D2Val:
        if i%2 != 0:
            sumD2Val += i
    sum = sumD2Val+ sumD1Val
    print(sum)
def sum_dictionaries(dict1,dict2):
    List1 = []
    List2 = []
    dict3 = {}
    for x,y in dict1.items():
        List1.append([x,y])
    for x,y in dict2.items():
        List2.append([x,y])
    if(len(List1)>len(List2)):
        for i in range(len(List1)):
            for j in range(len(List2)):
                if(List1[i][0]==List2[j][0]):
                    dict3.update({List1[i][0]:List1[i][1]+List2[j][1]})
    print(dict3)



    
def main():
    dict1 = {1:10, 2:20,3:30,4:40}
    dict2 = {1:21,3:63}
    find_max(dict1)
    merge_dictionaries(dict1,dict2)
    odd_sum_dictionaries(dict1,dict2)
    sum_dictionaries(dict1,dict2)
if __name__ == "__main__":
    main()