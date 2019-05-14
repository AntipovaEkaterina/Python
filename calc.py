# + - * /


while True:

    s = input("Enter operation:(+,-,*,/): ")
    if s == '0': break
    
    print("Enter numbers")
    a = int(input("a = "))
    b = int(input("b = "))

    if s in ('+','-','*','/'):
        if s == '+':
            print("%d" % (a+b))
        elif s == '-':
            print("%d" % (a-b))
        elif s == '*':
            print("%d" % (a*b))
        elif s == '/':
            print("%.3f" % (a/b))
        else:
            print("ERROR")
