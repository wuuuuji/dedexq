"""
在平面直角坐标系中，两点可以确定一条直线。如果有多点在一条直线上， 那么这些点中任意两点确定的直线是同一条。

给定平面上 2 × 3 个整点{(x, y)|0 ≤ x < 2, 0 ≤ y < 3, x ∈ Z, y ∈ Z}，即横坐标 是 0 到 1 (包含 0 和 1) 之间的整数、
纵坐标是 0 到 2 (包含 0 和 2) 之间的整数 的点。这些点一共确定了 11 条不同的直线。

给定平面上 20 × 21 个整点 {(x, y)|0 ≤ x < 20, 0 ≤ y < 21, x ∈ Z, y ∈ Z}，即横 坐标是 0 到 19 (包含 0 和 19) 之间的整数、
纵坐标是 0 到 20 (包含 0 和 20) 之 间的整数的点。请问这些点一共确定了多少条不同的直线。
"""
size = [[x, y]for x in range(20) for y in range(21)]
docker = set()
for i in size:
    x1, y1 = i[0], i[1]
    for j in size:
        x2, y2 = j[0], j[1]
        if x1 == x2:
            continue
        k = (y2 - y1)/(x2 -x1)
        b = (x2*y1 - x1*y2)/(x2 -x1)
        if (k, b) not in docker:
            docker.add((k, b))

print(len(docker)+20)
