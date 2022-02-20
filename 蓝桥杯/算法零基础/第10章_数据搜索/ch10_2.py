def binary_search(nLst):
    print("打印搜寻列表 : ",nLst)
    low = 0                     # 列表的最小索引
    high = len(nLst) - 1        # 列表的最大索引
    middle = int((high + low) / 2)  # 中间索引
    times = 0                   # 搜寻次数
    while True:
        times += 1
        if key == nLst[middle]: # 表示找到了
            rtn = middle
            break
        elif key > nLst[middle]:
            low = middle + 1    # 下一次往右边搜寻
        else:
            high = middle - 1   # 下依次往左边搜寻
        middle = int((high + low) / 2)  # 更新中间索引
        if low > high:          # 所有元素比较结束
            rtn = -1
            break
    return rtn, times

data = [19, 32, 28, 99, 10, 88, 62, 8, 6, 3]
sorted_data = sorted(data)      # 排序列表
key = int(input("请输入搜寻值 : "))
index, times = binary_search(sorted_data)
if index != -1:
    print("在索引 %d 位置找到了,共找了 %d 次" % (index, times))
else:
    print("查无此搜寻号码")