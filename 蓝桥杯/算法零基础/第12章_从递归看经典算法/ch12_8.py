from tkinter import *
def htree(order, center, ht):
    """ 依指定阶级数绘制 H 树分形 """
    if order >= 0:
        p1 = [center[0] - ht / 2, center[1] - ht / 2]   # 左上角
        p2 = [center[0] - ht / 2, center[1] + ht / 2]   # 左下角
        p3 = [center[0] + ht / 2, center[1] - ht / 2]   # 右上角
        p4 = [center[0] + ht / 2, center[1] + ht / 2]   # 右下角

        drawLine([center[0] - ht / 2, center[1]],
                 [center[0] + ht / 2, center[1]])   # 汇总H水平线
        drawLine(p1, p2)    # 汇总H左边垂直线
        drawLine(p3, p4)    # 汇总H右边垂直线

        htree(order - 1, p1, ht / 2)    # 递归左上点当中间点
        htree(order - 1, p2, ht / 2)    # 递归左下点当中间点
        htree(order - 1, p3, ht / 2)    # 递归右上点当中间点
        htree(order - 1, p4, ht / 2)    # 递归右下点当中间点

def drawLine(p1, p2):
    """ 绘制p1和p2之间的线条 """
    canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="htree")

def show():
    """ 显示 htree """
    canvas.delete("htree")
    length = 200
    center = [200, 200]
    htree(order.get(), center, length)

tk = Tk()
canvas = Canvas(tk, width=400, height=400)      # 建立画布
canvas.pack()
frame = Frame(tk)       # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame内建立标签Label, 输入阶乘数Entry, 按钮Button
Label(frame, text="输入阶数 : ").pack(side=LEFT)
order = IntVar()
order.set(0)
entry = Entry(frame, textvariable=order).pack(side=LEFT, padx=3)
Button(frame, text='显示 htree', command=show).pack(side=LEFT)
tk.mainloop()
