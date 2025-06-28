import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x = int(input())

    if x == 1:
        print(1)
        continue

    left, right = x, 2*x-1
    r = right

    while left <= right:
        mid = (left + right) // 2
        if mid % 2 == 0:
            mid += 1

        w = (mid + 1) // 2
        g = mid - (x-1)

        if g >= w:
            r = mid
            right = mid - 2
        else:
            left = mid + 2

    print(r)
