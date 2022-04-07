def subset_generator(data):
    final_subset = [[]]
    for item in data:
        final_subset.extend([subset + [item]for subset in final_subset])
    return final_subset


data = ['电视', '音响', '笔电']
value = [40000, 50000, 20000]
weight = [3, 4, 1]
bags = subset_generator(data)
max_value = 0       # 商品总值
for bag in bags:    # 处理组合商品
    if bag:     # 如果不是空集
        w_sum = 0   # 组合商品总重量
        v_sum = 0   # 组合商品总价值
        for b in bag:   # 拆解商品
            i = data.index(b)   # 了解商品
            w_sum += weight[i]  # 加总商品的数量
            v_sum += value[i]   # 加总商品的价值
            if w_sum <= 4:      # 如果商品总重量小于4千克
                if v_sum > max_value:    # 如果总价值大于目前最大价值
                    max_value = v_sum    # 更新最大价值
                    product = bag        # 记录商品


print('商品组合 = {}\n商品价值 = {}'.format(product, max_value))