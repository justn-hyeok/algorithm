n, m = map(int, input().split())

board = []
result = []

for i in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        w_count = 0
        b_count = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        w_count += 1
                    if board[k][l] != 'B':
                        b_count += 1
                else:
                    if board[k][l] != 'B':
                        w_count += 1
                    if board[k][l] != 'W':
                        b_count += 1
        result.append(min(w_count, b_count))

print(min(result)) 