def greedy(cs):
    length = len(cs)    # 课程数量
    course_list = []    # 存储结果
    course_list.append(cs[0])   # 第一节课
    course_end_time = course_list[0][1][1]      # 第一节课下课时间
    for i in range(1, length):      # 贪婪选课
        if cs[i][1][0] >= course_end_time:      # 上课时间晚于或等于
            course_list.append(cs[i])      # 加入贪婪选课
            course_end_time = cs[i][1][1]
    return course_list


course = {'化学': (12, 13),
          '英文': (9, 11),
          '数学': (8, 10),
          '计概': (10, 12),
          '物理': (11, 13),
          }

cs = sorted(course.items(), key=lambda item: item[1][1])
print('所有课程依下课时间排序如下')
print('课程', '    开始时间', '  下课时间')
for i in range(len(cs)):
    print("{0}{1:7d}:00{2:7d}:00".format(cs[i][0], cs[i][1][0], cs[i][1][1]))

s = greedy(cs)
print('贪婪排课时间如下')
print('课程', '    开始时间', '  下课时间')
for i in range(len(s)):
    print("{0}{1:7d}:00{2:7d}:00".format(s[i][0], s[i][1][0], s[i][1][1]))