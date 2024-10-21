fa = 1
fb = 1
print(fa)
print(fb)
for i in range(28):
    temp = fa + fb
    fa = fb
    fb = temp
    print(fb)