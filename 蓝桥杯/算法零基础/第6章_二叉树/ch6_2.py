def create_btree(tree: list, data: list):
    """使用data建立二叉树"""
    for i in range(len(data)):
        level: int = 0
        if i == 0:
            tree[level] = data[i]  # 第0索引数据放在第0层
        else:
            # 当while循环结束表示找到存放数据的节点(索引)位置
            while tree[level]:
                if data[i] > tree[level]:  # 如果数组不是0表示这是有数据可以比较
                    level = level * 2 + 2
                else:  # 否则往左找寻
                    level = level * 2 + 1
        tree[level] = data[i]
        print(i, tree)


btree = [0] * 8
data = [10, 21, 5, 9, 13, 28]
create_btree(btree, data)
for i in range(len(btree)):
    print("二叉树数组btree[%d] = %d" % (i, btree[i]))
