import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        a = sorted(int(input()) for _ in range(n))
        
        ans = None
        max_diff = -1
        
        l, r = 0, n-1
        while l < r:
            total = a[l] + a[r]
            if total < x:
                l += 1
            elif total > x:
                r -= 1
            else:
                diff = a[r] - a[l]  # abs() 제거 (이미 정렬되어 있음)
                if diff > max_diff:
                    max_diff = diff
                    ans = (a[l], a[r])
                l += 1
                r -= 1
        
        print(f'yes {ans[0]} {ans[1]}' if ans else 'danger')
    except:
        break