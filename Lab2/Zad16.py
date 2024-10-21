x = int(input("Podaj x:"))
if(x>99):
    print("Cyfra jedności: ", x%10)
    print("Cyfra dziesiątek: ", (x//10)%10)
    print("Cyfra setek: ", (x//100)%10)