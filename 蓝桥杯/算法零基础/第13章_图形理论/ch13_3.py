from collections import deque

people = deque()        # 建立queue
people.append('Ivan')   # 右边加入
people.append('Ira')    # 右边加入
print("列出名单 : ", people)
people.appendleft('Unistar')    # 右边加入
print("列出名单 : ", people)
people.appendleft('Ice Rain')    # 右边加入
print("列出名单 : ", people)