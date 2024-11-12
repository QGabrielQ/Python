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

    
def main():
    dict1 = {1:10,2:7,3:8,4:15,5:14,6:3,7:2}
    dict2 = {8:10,9:40,1:55}
    find_max(dict1)
    merge_dictionaries(dict1,dict2)
    odd_sum_dictionaries(dict1,dict2)
if __name__ == "__main__":
    main()