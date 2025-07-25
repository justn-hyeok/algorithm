n = int(input())
board = [''] * (n + 1)
board[0] = input()
flip = [[False] * n for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '#':
            if 0 < j:
                flip[i][j-1] = not flip[i][j-1]
            if j < n-1:
                flip[i][j+1] = not flip[i][j+1]
            if i < n-1:
                flip[i+1][j] = not flip[i+1][j]
    
    for j in range(n):
        if flip[i][j]:
            board[i+1] += '#'
        else:
            board[i+1] += '.'
    
    result.append(board[i])

print('\n'.join(result))