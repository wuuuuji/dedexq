def subset_generator(data):
    final_subset = [[]]
    for item in data:
        final_subset.extend([subset + [item] for subset in final_subset])
    return final_subset

data = ['释迦', '西瓜', '玉荷包', '苹果', '黑金刚', '西红柿']
value = [800, 200, 600, 700, 400, 100]
weight = [5, 3, 2, 2, 3, 1]
bags = subset_generator(data)
max_value = 0
for bag in bags:
    if bag:
        w_sum = 0
        v_sum = 0
        for b in bag:
            i = data.index(b)
            w_sum += weight[i]
            v_sum += value[i]
            if w_sum < 6:
                if v_sum > max_value:
                    max_value = v_sum
                    product = bag


print('商品组合 = {}\n商品价值 = {}'.format(product, max_value))