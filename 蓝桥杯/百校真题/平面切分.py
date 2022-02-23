import sys
n = int(input())
lines = []
for i in range(n):
    a, b = list(map(int, input().split()))
    lines.append((a, b))
lines = list(set(lines))#这里是去掉重复直线
n = len(lines)
def getnode(lines1, lines2):#得到两条直线交点，若平行，返回None
    A1 = lines1[0]
    B1 = lines1[1]
    A2 = lines2[0]
    B2 = lines2[1]
    if A1 - A2 == 0:
        return 
    x = (B2 - B1) / (A1 - A2)
    y = A1 * x + B1
    x = round(x, 10)
    y = round(y, 10)
    return (x, y)
ci = [1] * (n + 1)
node = set()
for i in range(1, n):
    node.clear()
    for j in range(i):
        tmp = getnode(lines[i], lines[j])
        if tmp == None: continue
        node.add(tmp)
    ci[i] += len(node)
        
print(sum(ci[:n]) + 1)        
