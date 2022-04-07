def subset_generator(data):
    ''' 子集生成函数, data须是可迭代对象 '''
    final_subset = [[]]
    for item in data:
        final_subset.extend([subset + [item] for subset in final_subset])
    return final_subset


data = ['a', 'b', 'c']
subset = subset_generator(data)
for s in subset:
    print(s)
