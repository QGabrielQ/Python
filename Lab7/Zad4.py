def find_max(dict):
    dictValues = list(dict.values())
    max = dictValues[0]
    for i in dictValues:
        if(i > max):
            max = i
    print(max)
        
    
def main():
    dict1 = {1:10,2:7,3:8,4:15,5:14,6:3,7:2}
    find_max(dict1)
if __name__ == "__main__":
    main()