class Queens:
    def __init__(self):
        self.queens = size * [-1]
        self.solve(0)
        for i in range(size):
            for j in range(size):
                if self.queens[i] == j:
                    print('★', end='')
                else:
                    print('☆', end='')
            print()

    def is_OK(self, row, col):
        """ 检查是否可以放在此row, col位置 """
        for i in range(1, row + 1):         # 循环往前检查是否冲突
            if (self.queens[row - i] == col     # 检查列
                or self.queens[row - i] == col-i    # 检查左上角斜线
                or self.queens[row - i] == col+i    # 检查右上角斜线
            ):
                return False    # 防护有冲突，不可使用
        return True     # 传回可以使用

    def solve(self, row):
        """ 从第 row 列开始寻找皇后的位置 """
        if row == size:     # 终止搜寻条件
            return True
        for col in range(size):
            self.queens[row] = col      # 安置(row, col)
            if self.is_OK(row, col) and self.solve(row + 1):
                return True
        return False


size = 8
Queens()