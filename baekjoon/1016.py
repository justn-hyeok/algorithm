a, b = map(int, input().split())

ans = b - a + 1
sieve = [False] * (b - a + 1)
i = 2

while i * i <= b:
    s = a // (i * i)
    if a % (i * i) != 0:
        s += 1

    while s * (i * i) <= b:
        if not sieve[s * (i * i) - a]:
            sieve[s * (i * i) - a] = True
            ans -= 1
        s += 1
    i += 1

print(ans)