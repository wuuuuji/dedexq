from tkinter import *
import math

def koch(order, p1, p2):
    ''' 绘制科赫雪花碎形(Fractal) '''
    if order == 0:                  # 如果阶层是0绘制线条
        drawLine(p1, p2)
    else:                           # 计算线段间的x, y, z点
        dx = p2[0] - p1[0]          # 计算线段间的x轴距离
        dy = p2[1] - p1[1]          # 计算线段间的y轴距离
# x是1/3线段点, y是2/3线段点, z是突出点
        x = [p1[0] + dx / 3, p1[1] + dy / 3]
        y = [p1[0] + dx * 2 / 3, p1[1] + dy * 2 / 3]
        z = [(int)((p1[0]+p2[0]) / 2 - math.cos(math.radians(30)) * dy / 3),
          (int)((p1[1]+p2[1]) / 2 + math.cos(math.radians(30)) * dx / 3)]
        # 递归调用绘制科赫雪花碎形
        koch(order - 1, p1, x)
        koch(order - 1, x, z)
        koch(order - 1, z, y)
        koch(order - 1, y, p2)

# 绘制p1和p2之间的线条
def drawLine(p1, p2):
    canvas.create_line(p1[0], p1[1], p2[0], p2[1],tags="myline")

# 显示koch线段
def koch_demo():
    canvas.delete("myline")
    p1 = [200, 20]
    p2 = [20, 300]
    p3 = [380, 300]
    order = depth.get()
    koch(order, p1, p2)             # 上方点到左下方点
    koch(order, p2, p3)             # 左下方点到右下方点
    koch(order, p3, p1)             # 右下方点到上方点

# main
tk = Tk()
myWidth = 400
myHeight = 400
canvas = Canvas(tk, width=myWidth, height=myHeight)
canvas.pack()

frame = Frame(tk)                   # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame内建立标签Label, 输入order数Entry, 按钮koch
Label(frame, text="输入order : ").pack(side=LEFT)
depth = IntVar()
depth.set(0)
entry = Entry(frame, textvariable=depth).pack(side=LEFT,padx=3)
Button(frame, text="koch",command=koch_demo).pack(side=LEFT)

koch_demo()                         # 第一次启动
tk.mainloop()