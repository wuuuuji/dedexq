from tkinter import *
import math


def paintTree(depth, x1, y1, length, angle):
    if depth >= 0:
        depth -= 1
        x2 = x1 + int(math.cos(angle) * length)
        y2 = y1 - int(math.sin(angle) * length)
        # 绘线
        drawLine(x1, y1, x2, y2)
        # 绘左边
        paintTree(depth, x2, y2, length * sizeRatio, angle + angleValue)
        # 绘右边
        paintTree(depth, x2, y2, length * sizeRatio, angle - angleValue)


def drawLine(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, tags="myline")

    # 显示


def show():
    canvas.delete("myline")
    myDepth = depth.get()
    paintTree(myDepth, myWidth / 2, myHeight, myHeight / 3, math.pi / 2)

    # main


tk = Tk()
myWidth = 400
myHeight = 400
canvas = Canvas(tk, width=myWidth, height=myHeight)  # 建立画布
canvas.pack()

frame = Frame(tk)  # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame内建立标签Label, 输入depth数Entry, 按钮Button
Label(frame, text="输入depth : ").pack(side=LEFT)
depth = IntVar()
depth.set(0)
entry = Entry(frame, textvariable=depth).pack(side=LEFT, padx=3)
Button(frame, text="Recursive Tree",
       command=show).pack(side=LEFT)
angleValue = math.pi / 4  # 设定角度
sizeRatio = 0.6  # 设定下一层的长度与前一层的比率是0.6

tk.mainloop()