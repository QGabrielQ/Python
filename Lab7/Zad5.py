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

    
def main():
    dict1 = {1:10,2:7,3:8,4:15,5:14,6:3,7:2}
    dict2 = {8:10,9:40,1:55}
    find_max(dict1)
    merge_dictionaries(dict1,dict2)
if __name__ == "__main__":
    main()