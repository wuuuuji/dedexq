n = int(input())
list_num = list(map(int, input().split()))
a = int(input())

try:
    print(list_num.index(a)+1)
except:
    print(-1)