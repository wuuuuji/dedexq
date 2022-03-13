x = input("in:")
flag = True
l = len(x) // 2

for i in range(l):
    if x[i] != x[-i-1]:
        flag = False
        break

if flag:
    print("YES")
else:
    print("No")