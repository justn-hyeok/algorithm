import sys

N, C = map(int, sys.stdin.readline().split())

A, B = N, N

for _ in range(C):
    X, Y = map(int, sys.stdin.readline().split())

    if X >= A or Y >= B:
        continue

    garo = X * B
    sero = Y * A

    if garo >= sero:
        A = X
    else:
        B = Y

print(A * B)
