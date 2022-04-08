import math
film = [5, 7, 8, 10, 2]
film_titles = ['复仇者联盟',
              '决战中途岛',
              '冰雪奇缘',
              '双子杀手']
film_features = [[2, 8, 8, 5, 6],
                 [5, 6, 9, 2, 5],
                 [8, 2, 0, 0, 10],
                 [5, 8, 8, 8, 3]]
dist = []
for f in film_features:
    distances = 0
    for i in range(len(f)):
        distances += (film[i] - f[i]) ** 2
    dist.append(math.sqrt(distances))

min = min(dist)  # 求最小值
min_index = dist.index(min)  # 最小值的索引

print("与玩命关头最相似的电影 : ", film_titles[min_index])
print("相似度值 : ", dist[min_index])
for i in range(len(dist)):
    print("影片 : %s, 相似度 : %6.2f" % (film_titles[i], dist[i]))