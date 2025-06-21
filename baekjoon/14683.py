import sys

sx, sy = map(int, sys.stdin.readline().split())
ex, ey = map(int, sys.stdin.readline().split())
b = int(sys.stdin.readline())

distance = abs(sx - ex) + abs(sy - ey)

if b < distance or (b - distance) % 2 != 0:
    print("N")
else:
    print("Y")
