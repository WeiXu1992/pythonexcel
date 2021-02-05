'''测试一个经典的GUI程序的写法，使用面向对象的方式'''

from tkinter import *
from tkinter import messagebox
class Application(Frame):
    """一个经典的GUI类的写法"""

    def __init__(self,master=None):
        super().__init__(master)        # super()代表的是父类的定义，而不是父类的对象
        self.master = master
        self.pack()

        self.CreatWidget()

    def CreatWidget(self):
        """创建组件"""
        self.btn01 = Button(self)
        self.btn01["text"] = "点击送花"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

        # 创建一个退出按钮
        self.btnQuit = Button(self,text = "退出", command = root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花","送你一朵玫瑰花")


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+100+200")  # 表达式符号之间不允许空格
    root.title("这是一个测试程序")
    app = Application(master=root)

    root.mainloop()

