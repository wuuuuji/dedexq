def greedy(s):
    length = len(cs)
    course_list = []
    course_list.append(cs[0])
    course_end_time = course_list[0][1][1]
    for i in range(1, length):
        if cs[i][1][0] >= course_end_time:
            course_list.append(cs[i])
            course_end_time = cs[i][1][1]
    return course_list


course = {'化学': (12, 13), '英文': (9, 11), '数学': (8, 10),
          '计概': (10, 12), '物理': (11, 13), '会计': (8, 9),
          '统计': (13, 14), '音乐': (14, 15), '美术': (12, 13)
          }
cs = sorted(course.items(), key=lambda item: item[1][1])
print('所有课程依下课时间排序如下')
print('课程', '    开始时间', '  下课时间')
for i in range(len(cs)):
    print("{0}{1:7d}:00{2:7d}:00".format(cs[i][0], cs[i][1][0], cs[i][1][1]))


cs1 = greedy(cs)
print('贪婪排课时间如下')
print('课程', '    开始时间', '  下课时间')
for i in range(len(cs1)):
    print("{0}{1:7d}:00{2:7d}:00".format(cs1[i][0], cs1[i][1][0], cs1[i][1][1]))