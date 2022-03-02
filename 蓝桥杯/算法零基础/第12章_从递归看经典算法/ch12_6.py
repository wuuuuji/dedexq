def is_OK(row, col):
    """ 检查是否可以放在此row, col位置 """
    for i in range(1, row+1):               # 循环往前检查是否冲突
        if(queens[row - i] == col           # 检查列
            or queens[row - i] == col - i   # 检查左上角斜线
            or queens[row - i] == col + i   # 检查右上角斜线
        ):
            return False    # 返回有冲突，不可使用
    return True     # 返回可以使用

def location(row):
    """ 搜寻特定row的col字段 """
    start = queens[row] + 1         # 也行是回溯，所有start不一定是0
    for col in range(start, SIZE):
        if is_OK(row, col):
            return col      # 暂时可以在(row, col)放置皇后
    return -1       # 没有适合位置所以回传 -1

def solve():
    """ 从特定row列开始找寻皇后的位置 """
    row = 0
    while 0 <= row <= 7:
        col = location(row)
        if col < 0:
            queens[row] = -1
            row -= 1
        else:
            queens[row] = col
            row += 1
    if row == -1:
        return False
    else:
        return True


SIZE = 8
queens = [-1] * SIZE
solve()
for i in range(SIZE):
    for j in range(SIZE):
        if queens[i] == j:
            print('★', end='')
        else:
            print('☆', end='')
    print()
