while 1:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == '?':break
    elif op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    #//は小数点切り捨ての割り算
    elif op == '/':
        print(a // b)