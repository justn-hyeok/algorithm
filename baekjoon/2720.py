t = int(input())
m = [25,10,5,1]

for _ in range(t):
  result = []
  n = int(input())

  for i in m:
    result.append(str(n//i))
    n %= i

  print(' '.join(result))
