X = int(input())
N = int(input())

t = X

for _ in range(N):
    used = int(input())
    t = t - used + X

print(t)
