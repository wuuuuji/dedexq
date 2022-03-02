"""如果一个分数的分子和分母的最大公约数是 1，这个分数称为既约分数。

例如 3/4 , 1/8, 7/1都是既约分数。

请问，有多少个既约分数，分子和分母都是 1 到 2020 之间的整数（包括 1 和 2020）？"""


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
ans = 0
for zi in range(1, 2021):
    for mu in range(1, 2021):
        if gcd(zi, mu) == 1:
            ans += 1
print(ans)
