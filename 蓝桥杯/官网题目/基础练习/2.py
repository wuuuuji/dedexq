a = int(input())
b = input().split()
b = list(map(int,b))
for i in range(a):
    for j in range(a-i-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
for i in range(a):
    print(b[i], end=" ")