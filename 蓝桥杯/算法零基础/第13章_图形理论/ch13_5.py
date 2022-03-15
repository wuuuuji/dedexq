from collections import deque

def banana_dealer(name):
    """ 回应是不是卖香蕉的经销商 """
    if name == 'Banana':
        return True

def search(name):
    """ 搜寻卖香蕉的朋友 """
    global not_dealer       # 储存已搜寻的名单
    dealer = deque()
    dealer += graph[name]       # 搜寻列表先储存Tom的朋友
    while dealer:
        person = dealer.popleft()   # 从左边取数据
        if banana_dealer(person):   # 如果Ture，表示找到了
            print(person + " 是香蕉经销商")
            return True     # search()执行结束
        else:
            not_dealer.append(person)   # 将搜寻过的人储存至列表
            dealer += graph[person]     # 将不是经销商的朋友加入
    print('没有找到经销商')
    return False


not_dealer = []
graph = {'Tom':['Ivan', 'Ira', 'Kevin'],
         'Ivan':['Peter'],
         'Ira':['Banana'],
         'Kevin':['Mary'],
         'Peter':[],
         'Banana':[],
         'Mary':[]
        }

search('Tom')
print('列出已搜寻名单 : ', not_dealer)