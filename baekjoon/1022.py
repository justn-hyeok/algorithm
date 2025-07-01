# 소용돌이 중심에서 좌표까지의 값을 계산하는 함수
def get_spiral_value(row, col):
    current_value = 1

    if row <= 0:
        if row <= col <= abs(row):    # 상단 영역
            step = 3
            for _ in range(-row):
                current_value += step
                step += 8
            current_value -= col
            return current_value
    else:
        if -row <= col <= abs(row):    # 하단 영역
            step = 7
            for _ in range(row):
                current_value += step
                step += 8
            current_value += col
            return current_value

    if col <= 0:    # 좌측 영역
        step = 5
        for _ in range(-col):
            current_value += step
            step += 8
        current_value += row
        return current_value
    else:           # 우측 영역
        step = 1
        for _ in range(col):
            current_value += step
            step += 8
        current_value -= row
        return current_value


start_row, start_col, end_row, end_col = map(int, input().split())

max_width = len(str(max(
    get_spiral_value(start_row, start_col),
    get_spiral_value(start_row, end_col),
    get_spiral_value(end_row, start_col),
    get_spiral_value(end_row, end_col)
)))

for row in range(start_row, end_row + 1):
    for col in range(start_col, end_col + 1):
        print(str(get_spiral_value(row, col)).rjust(max_width), end=' ')
    print()
