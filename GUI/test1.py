from tkinter import *
from tkinter import messagebox

root = Tk()

btn01 = Button(root)

root.title("这是第一个GUI程序")
root.geometry("500x300+100+200")  # 500x300设置窗口大小，100左边距，200上边距

btn01["text"] = "点我就送花"
btn01.pack()


def songhua(e):
    messagebox.showinfo("message", "送你一朵花")


btn01.bind("<Button-1>", songhua)

root.mainloop()  # 调用mainloop进入事件循环
