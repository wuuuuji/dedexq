def Letter(n, m):
    var = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if 1 <= n <= 26 and 1 <= m <= 26:
        for i in range(n):
            rear = var[1:i + 1]  # BC
            font = var[0:m - i]  # ABCDE
            s = rear[::-1] + font
            print(s[0:m])  # 防止出现一行多于m个字母的情况


n, m = map(int, input().split())  # 输入格式，输入一行
Letter(n, m)

'''
string_list = ['A', 'B', 'C', 'D', 'E', 'F',
              'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R',
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


outlist = []
templist = []
flag = 0
a = input().split()
n = int(a[0])  # 行
m = int(a[1])  # 字符

if m == 1:
    for i in range(n):
        print("A")
elif m == 2:
    for i in range(m):
        outlist.append(string_list[i])
    while flag < n:
        for i in range(m):
            print(outlist[i], end='')
        print()
        templist.insert(0, outlist.pop())
        outlist.insert(0, templist.pop())
        flag += 1
elif 3 <= m <= 26:
    for i in range(m):
        outlist.append(string_list[i])
        templist.insert(0, string_list[i])
    del templist[0]
    del templist[m - 2]
    while flag < n:
        for i in range(m):
            print(outlist[i], end='')
        print()
        outlist.insert(0, templist.pop())
        templist.insert(0, outlist.pop())
        flag += 1
'''
