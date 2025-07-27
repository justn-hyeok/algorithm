while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        a = [int(input()) for _ in range(n)]
        a.sort()
        
        ans = None
        max_diff = -1
        
        l, r = 0, n-1
        while l < r:
            if a[l] + a[r] < x:
                l += 1
            elif a[l] + a[r] > x:
                r -= 1
            else:
                diff = abs(a[l] - a[r])
                if diff > max_diff:
                    max_diff = diff
                    ans = (a[l], a[r])
                l += 1
                r -= 1
        
        if ans:
            print(f'yes {ans[0]} {ans[1]}')
        else:
            print('danger')
    except:
        break