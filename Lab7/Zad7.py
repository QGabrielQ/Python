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
    sum = 0 
    for y in dict1.values():
        if y%2 == 1:
            sum += y
    for y in dict2.values():
        if y%2 == 1:
            sum += y
    print(sum)
def sum_dictionaries(dict1,dict2):
    dict3 = {}
    for x1,y1 in dict1.items():
        for x2,y2 in dict2.items():
            if(x1 == x2):
                dict3.update({x1: y1+y2})
    print(dict3)


    
def main():
    dict1 = {1:10, 2:20, 3:30, 4:40}
    dict2 = {1:11,3:33,5:55}
    find_max(dict1)
    merge_dictionaries(dict1,dict2)
    odd_sum_dictionaries(dict1,dict2)
    sum_dictionaries(dict1,dict2)
if __name__ == "__main__":
    main()