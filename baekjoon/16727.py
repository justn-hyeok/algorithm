p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

p_total = p1 + p2
s_total = s1 + s2

if p_total > s_total:
    print("Persepolis")
elif s_total > p_total:
    print("Esteghlal")
else:
    if p2 > s1:
        print("Persepolis")
    elif s1 > p2:
        print("Esteghlal")
    else:
        print("Penalty")
