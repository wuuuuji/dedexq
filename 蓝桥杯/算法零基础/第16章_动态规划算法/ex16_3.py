def knapsack(bg, w, val):
    n = len(val)
    table = [[0 for x in range(bg + 1)] for x in range(n + 1)]  # 最初化表格
    items = [[[] for x in range(bg + 1)] for x in range(n + 1)]
    for r in range(n + 1):
        for c in range(bg + 1):
            if r == 0 or c == 0:
                table[r][c] = 0
            elif w[r - 1] <= c:
                cur = val[r - 1] + table[r - 1][c - w[r - 1]]
                cur_items = []
                cur_items.append(data[r - 1])
                if items[r - 1][c - w[r - 1]]:
                    cur_items += items[r - 1][c - w[r - 1]]
                pre = table[r - 1][c]
                pre_items = items[r - 1][c]
                if cur > pre:
                    table[r][c] = cur
                    items[r][c] = cur_items
                else:
                    table[r][c] = pre
                    items[r][c] = pre_items
            else:
                table[r][c] = table[r - 1][c]
                items[r][c] = items[r - 1][c]
    return items, table[n][bg]



data = ['笔电', '音响', '电视', '手机']
value = [20000, 50000, 40000, 25000]
weight = [1, 4, 3, 1]
bag_weight = 4
itmes, total_value = knapsack(bag_weight, weight, value)
print('商品价值 : ', total_value)
print('商品组合 : ', itmes[len(data)][bag_weight])