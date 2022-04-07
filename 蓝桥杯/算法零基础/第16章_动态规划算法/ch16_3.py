def knapsack(bg, w, val):
    n = len(val)
    table = [[0 for x in range(bg+1)] for x in range(n+1)]  # 最初化表格
    for r in range(n+1):
        for c in range(bg + 1):
            if r == 0 or c == 0:
                table[r][c] == 0
            elif w[r-1] <= c:
                table[r][c] = max(val[r-1] + table[r-1][c-w[r-1]], table[r-1][c])
            else:
                table[r][c] = table[r-1][c]
    return table[n][bg]


value = [20000, 50000, 40000, 25000]    # 商品价值
weight = [1, 4, 3, 1]   # 商品重量
bag_weight = 4  # 背包可容纳重量
print('商品价值 : ', knapsack(bag_weight, weight, value))