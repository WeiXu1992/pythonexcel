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
        self.label01 = Label(self,text = "苦逼程序猿",width=10,height=2,
                             bg="black",fg="white")
        self.label01.pack()

        self.label02 = Label(self,text = "小傻逼",width=10,height=2,
                             bg="blue",fg="white",font=("黑体", 30))
        self.label02.pack()

        # 显示图像
        global photo # 把photo声明成全局变量，如果是局部变量，本方法执行完毕后，图像对象销毁，窗口显示不出图像
        photo = PhotoImage(file="./gif1.gif")
        self.label03 = Label(self,image=photo)
        self.label03.pack()

        self.label04 = Label(self,text="北京\n广州\n上海\n苦逼的地方，有钱的一笔",
                             borderwidth=1,relief="solid",justify="right")
        self.label04.pack()

    # def songhua(self):
    #     messagebox.showinfo("送花","送你一朵玫瑰花")


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x800+100+100")  # 表达式符号之间不允许空格
    root.title("这是一个测试程序")
    app = Application(master=root)

    root.mainloop()

