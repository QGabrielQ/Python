def Pole_Prost(a,b):
    assert a > 0, "Ujemne liczby!!"
    assert b > 0, "Ujemne liczby!!"
    return a*b
print(Pole_Prost(5,10))
print(Pole_Prost(-5,10))
