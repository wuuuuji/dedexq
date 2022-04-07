''' 背包问题 '''


def greedy(th):
    length = len(th)
    things_list = []
    things_list.append(th[length - 1])
    weight = th[length - 1][1][1]
    for i in range(length - 1, -1, -1):
        if th[i][1][1] + weight <= max_wight:
            things_list.append(th[i])
            weight += th[i][1][1]
    return things_list


things = {'iWatch手表': (15000, 0.1),
          'Asus  笔电': (35000, 0.7),
          'iPhone手机': (38000, 0.3),
          'Acer  笔电': (40000, 0.8),
          'Go Pro摄影': (12000, 0.1),
          }

max_wight = 1
th = sorted(things.items(), key=lambda item: item[1][0])
print('所有商品依价值间排序如下')
print('商品', '          商品价格', '   商品重量')
for i in range(len(th)):
    print("{0}{1:10d}{2:10.2f}".format(th[i][0], th[i][1][0], th[i][1][1]))

t = greedy(th)
print('贪婪选择商品如下')
for i in range(len(t)):
    print("{0}{1:10d}{2:10.2f}".format(t[i][0], t[i][1][0], t[i][1][1]))
