"""
小蓝最近学习了一些排序算法，其中冒泡排序让他印象深刻。
在冒泡排序中，每次只能交换相邻的两个元素。
小蓝发现，如果对一个字符串中的字符排序，只允许交换相邻的两个字符，在所有可能的排序方案中，冒泡排序的总交换次数是最少的。
例如，对于字符串 lan 排序，只需要 1 次交换。对于字符串 qiao 排序，总共需要 4 次交换。
小蓝的幸运数字是 VV，他想找到一个只包含小写英文字母的字符串，对这个串中的字符进行冒泡排序，正好需要 VV 次交换。
请帮助小蓝找一个这样的字符串。如果可能找到多个，请告诉小蓝最短的那个。如果最短的仍然有多个，请告诉小蓝字典序最小的那个。
请注意字符串中可以包含相同的字符。
"""
def bubble(t):
    s = t.copy()
    cnt = 0
    for i in range(len(s)-1):
        for j in range(len(s)-1-i):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                cnt += 1
    return cnt


s = []
for i in range(26):
    s.insert(0, chr(97+i))
    cnt = bubble(s)
    if cnt >= 100:
        break

for i in range(2, len(s)-1):
    tmp = list(s[-i])+s[:-i]+s[-i+1:]
    if bubble(tmp) >= 100:
        print(''.join(tmp))
        print(bubble(tmp))
        break

