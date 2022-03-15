n = int(input())
template = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    l, r, k = map(int, input().split())
    tem = template[l-1:r]
    for i in range(k-1):
        tem.pop(tem.index(max(tem)))
    else:
        print(max(tem))
