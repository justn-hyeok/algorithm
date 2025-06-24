n = int(input())

if n == 0:
    print(1)
elif n > 0:
    print(len(bin(n))-2)
else:
    a = (1 << 32) + n
    delete0b = bin(a)[2:]
    first1 = delete0b.find('1')
    if first1 == -1:
        print(1)
