import sys

p = int(sys.stdin.readline().strip())

for _ in range(p):
    line = sys.stdin.readline().strip().split()
    k = int(line[0])
    n = int(line[1])

    total_candles = (n * (n + 1)) // 2 + n

    print(k, total_candles)
