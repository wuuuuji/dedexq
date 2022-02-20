def sequentialSearch(nLst):
    for i in range(len(nLst)):
        if nLst[i] == key:      # 找到了
            return i            # 传回索引值
    return -1                   # 找不到传回-1

nameLst = []
while True:
    name = input("请输入姓名(Q或q代表输入结束) : ")
    if name == "Q" or name == "q":
        break
    nameLst.append(name)

key = input("请输入搜寻姓名 : ")
rtn = sequentialSearch(nameLst)
if rtn != -1:
    print("在索引 %d 位置找到了 %s 共找了 %d 次" % (rtn+1, key, (rtn+1)))
else:
    print("查无此搜寻姓名")