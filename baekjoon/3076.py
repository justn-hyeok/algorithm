R, C = map(int, input().split())
A, B = map(int, input().split())

# 체스판의 기본 패턴 생성 (R x C 크기)
for i in range(R * A):
    for j in range(C * B):
        # 현재 위치가 속한 체스판의 블록 위치 계산
        block_row = i // A
        block_col = j // B

        # 블록의 색상 결정 (블록 위치의 합이 짝수면 X, 홀수면 .)
        if (block_row + block_col) % 2 == 0:
            print('X', end='')
        else:
            print('.', end='')
    print()  # 줄 바꿈
