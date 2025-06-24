n=int(input())
print(1 if n==0 else len(bin(n+(1<<32)*(n<0))[2:].lstrip('0'or'1')))
