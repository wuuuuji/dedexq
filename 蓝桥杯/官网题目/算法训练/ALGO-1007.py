"""
共有n种图案的印章，每种图案的出现概率相同。小A买了m张印章，求小A集齐n种印章的概率。
"""

l = [eval(x) for x in input().split()]


def P(n, m):
    dp = [[0, 1] + [0] * (n - 1) for i in range(m + 1)]
    for i in range(2, m + 1):
        for j in range(1, n + 1):
            choose = n - (j - 1)
            dp[i][j] = dp[i - 1][j] * j / n + dp[i - 1][j - 1] * choose / n
    return dp[m][n]


print(format(P(l[0], l[1]), ".4f"))
