from collections import deque


def banan_dealer(name):
    if name == 'Banana':
        return True


def search(name):
    global not_dealer
    dealer = deque()
    dealer += graph[name]
    print("目前搜寻列表名单 : ", dealer)
    while dealer:
        person = dealer.popleft()
        if banan_dealer(person):
            print(person + " 是香蕉经销商")
            return True
        else:
            print(person + " 不是是香蕉经销商")
            not_dealer.append(person)
            dealer += graph[person]
            print("目前搜寻列表名单 : ", dealer)
    print('没有找到经销商')
    return False


not_dealer = []
graph = {'Tom': ['Ivan', 'Ira', 'Kevin'],
         'Ivan': ['Peter'],
         'Ira': ['Banana'],
         'Kevin': ['Mary'],
         'Peter': [],
         'Banana': [],
         'Mary': []
         }

search('Tom')
print('列出已搜寻名单 : ', not_dealer)