def knapsack(bg, w, val):
    n = len(val)
    table = [[0 for x in range(bg+1)] for x in range(n+1)]  # 最初化表格
    items = [[[] for x in range(bg+1)] for x in range(n+1)]
    for r in range(n+1):
        for c in range(bg + 1):
            if r == 0 or c == 0:
                table[r][c] == 0
            elif w[r-1] <= c:
                cur = val[r-1] + table[r-1][c-w[r-1]]
                cur_items = []
                cur_items.append(data[r-1])
                if items[r-1][c-w[r-1]]:
                    cur_items += items[r-1][c-w[r-1]]
                pre = table[r-1][c]
                pre_items = items[r-1][c]
                if cur > pre:
                    table[r][c] = cur
                    items[r][c] = cur_items
                else:
                    table[r][c] = pre
                    items[r][c] = pre_items
            else:
                table[r][c] = table[r-1][c]
                items[r][c] = items[r-1][c]
    return items, table[n][bg]


data = ['释迦', '西瓜', '玉荷包', '苹果', '黑金刚', '西红柿']
value = [800, 200, 600, 700, 400, 100]
weight = [5, 3, 2, 2, 3, 1]
bag_weight = 5  # 背包可容纳重量
items, total_value = knapsack(bag_weight, weight, value)
print('最高价值 : ', total_value)
print('商品组合 : ', items[len(data)][bag_weight])