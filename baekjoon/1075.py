N = int(input())
F = int(input())

base = N // 100 * 100

for i in range(100):
    num = base + i
    if num % F == 0:
        print(f"{i:02d}")
        break