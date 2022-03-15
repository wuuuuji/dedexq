from collections import deque

graph = {}      # 建立空字典
graph['Tom'] = ['Ivan', 'Ira', 'Kevin']     # 建立字典graph, key='Tom'的值
people = deque()        # 建立queue
people += graph["Tom"]      # 将graph字典Tom键的值加入people
print('列出people数据类型: ', type(people))
print('列出搜寻名单      : ', people)
for name in range(len(people)):
    print(people.pop())
