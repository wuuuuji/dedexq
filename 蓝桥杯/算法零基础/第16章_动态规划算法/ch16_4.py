def traveling(tw, w, val):
    n = len(val)
    table = [[0 for x in range(tw + 1)] for x in range(n + 1)]
    for r in range(n + 1):
        for c in range(tw + 1):
            if r == 0 or c == 0:
                table[r][c] = 0
            elif w[r-1] <= c:
                table[r][c] = max(val[r-1] + table[r-1][c-w[r-1]], table[r-1][c])
            else:
                table[r][c] = table[r-1][c]
    return table[n][tw]


value = [7, 6, 9, 9, 8]
weight = [1, 1, 2, 4, 1]
travel_weight = 4
print('旅行点评总分 = ', traveling(travel_weight, weight, value))