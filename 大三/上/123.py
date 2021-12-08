import tkinter as tk
from tkinter import DISABLED

top = tk.Tk()
top.title("asd")

money = 0
money2 = 0
money3 = 0

def bbq():
    print("bbq")
    money = money2 + 1

    print(money)


def p1():
    btn1.configure(state=DISABLED)


def p2():
    btn2.configure(state=DISABLED)


def p3():
    btn3.configure(state=DISABLED)


btn1 = tk.Button(top, text="1", bg='Cyan', command=lambda: [bbq(), p1()])
btn2 = tk.Button(top, text="1", bg='yellow', command=lambda: [bbq(), p2()])
btn3 = tk.Button(top, text="1", bg='white', command=lambda: [bbq(), p3()])
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=1, column=1)
top.mainloop()