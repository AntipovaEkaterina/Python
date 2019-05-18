# 0 1 1 2 3 5 8 13 ... 100

a = 0
b = 1

print (a)
print (b)

while (a + b <= 100):
    b = a + b
    a = b - a
    print (b)

