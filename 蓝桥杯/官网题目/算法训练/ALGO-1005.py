"""
给定一个1～N的排列a[i]，每次将相邻两个数相加，得到新序列，再对新序列重复这样的操作，显然每次得到的序列都比上一次的序列长度少1，最终只剩一个数字。
　　例如:
　　3 1 2 4
　　4 3 6
　　7 9
　　16
　　现在如果知道N和最后得到的数字sum，请求出最初序列a[i]，为1～N的一个排列。若有多种答案，则输出字典序最小的那一个。数据保证有解。
"""
a, b = map(int, input().split())
final = [[b]]
for i in range(a):
    tem = []
    for j in final[-1]:
        tnum = j // 2
        tem.append(tnum)
        tem.append(j - tnum)
    final.append(tem)

print(final)