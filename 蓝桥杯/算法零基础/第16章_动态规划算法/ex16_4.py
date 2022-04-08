def knapsack(bg, w, val):
    n = len(val)
    table = [[0 for x in range(bg+1)] for x in range(n+1)]
    items = [[[] for x in range(bg+1)] for x in range(n+1)]
    for r in range(n+1):
        for c in range(bg+1):
            if r == 0 or c == 0:
                table[r][c] = 0
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
                table[r][c] = table[r - 1][c]
                items[r][c] = items[r - 1][c]
    return items, table[n][bg]


data = ['颐和园', '天坛', '故宫', '万里长城', '圆明园']
value = [7, 6, 9, 9, 8]
weight = [1, 1, 2, 4, 1]
max_weight = 4
items, total_value = knapsack(max_weight, weight, value)
print('最高价值 : ', total_value)
print('商品组合 : ', items[len(data)][max_weight])