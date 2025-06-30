from math import sqrt

def dist(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

xa, ya, xb, yb, xc, yc = map(int, input().split())

if (xb-xa)*(yc-ya) == (yb-ya)*(xc-xa):
    print(-1.0)
else:
    d1 = dist(xa, ya, xb, yb)  # AB
    d2 = dist(xb, yb, xc, yc)  # BC
    d3 = dist(xc, yc, xa, ya)  # CA

    p1 = 2 * (d1 + d2)  # AB와 BC가 변
    p2 = 2 * (d2 + d3)  # BC와 CA가 변
    p3 = 2 * (d3 + d1)  # CA와 AB가 변

    result = max(p1, p2, p3) - min(p1, p2, p3)
    print(result)
