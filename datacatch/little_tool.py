from tkinter import *  # 导入 Tkinter 库
from  tkinter import scrolledtext #导入scrolledtext库
import requests #导入resquests库
from bs4 import BeautifulSoup #导入BeautifulSoup库
from urllib.parse import quote

root = Tk()  # 创建窗口对象的背景色

def getsearchword():
    keyword = entry.get()
    word = quote(keyword, 'utf-8')

entry = Entry(root) #文本输入框
entry.grid(row = 0,column = 0,ipadx = 90,padx=10,pady=5,sticky=W)#文本输入框
button = Button(root, text="搜索",command = getsearchword).grid(row=0,column=1,padx=10,pady=5,sticky=E)#搜索按钮
scrolW = 51 # 设置文本框的长度
scrolH = 15 # 设置文本框的高度
listcontent = scrolledtext.ScrolledText(root,width=scrolW, height=scrolH, wrap=WORD)#内容显示列表，使用到了tkinter内置的scrolledtext--滚动文本框
listcontent.grid(column=0, columnspan=2)

#设置基本参数
def setParams():
    root.title('文库小帮手器')#设置title
    root.geometry('400x250')#设置大小

if __name__ == '__main__':
    setParams()
    root.mainloop()  # 进入消息循环