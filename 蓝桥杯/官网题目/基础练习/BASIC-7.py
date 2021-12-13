def cubic(a: int) -> int:
    a3 = a * a * a
    return a3


for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            temp = str(i) + str(j) + str(k)
            if cubic(i) + cubic(j) + cubic(k) == int(temp):
                print(temp)

i = 100
while i < 1000:
    if i == (i % 10) ** 3 + (i // 10 % 10) ** 3 + (i // 100) ** 3:
        print(i)
    i = i + 1
