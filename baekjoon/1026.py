n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sort_a = sorted(a, reverse=True)
sort_b = sorted(b)

s = 0
for i in range(n):
    s += sort_a[i] * sort_b[i]

print(s)