'''
PyQt5 中QLable 控件

setIndent():设置文本的对齐方式

text(): 获取文本内容

setBuddy():设置伙伴关系

setText():设置文本内容

selectedText():返回所选择的字符

setWordWrap():设置是否允许换行

QLabel 常用的信号(事件):

1.档鼠标滑过QLabel控件时触发LinkHovered
2.当鼠标单击QLabel控件时触发LinkClicked
'''
import sys
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QToolBox, QApplication, QPushButton, QWidget, QLabel
from PyQt5.QtGui import QFont, QPalette, QPixmap           # QPalette是调色板
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个黄色标签.</font>")
        label1.setAutoFillBackground(True)
        paletle = QPalette()
        paletle.setColor(QPalette.Window,Qt.blue)   # 设置背景色
        label1.setPalette(paletle)
        label1.setAlignment(Qt.AlignCenter)     # 设置文字的对齐方式


        label2.setText("<a href='#'>欢迎使用python Gui程序")

        label3.setAlignment(Qt.AlignCenter)

        label3.setToolTip('这是一个图片标签')

        label3.setPixmap(QPixmap("./f1.ico"))   # 设置图像

        label4.setOpenExternalLinks(True)   # 如果设置为真，则可以打开默认浏览器，如果为假，则调用槽函数
        label4.setText("<a href='https://github.com/WeiXu1992/pythonexcel1'>感谢使用python教程")

        label4.setAlignment(Qt.AlignRight)

        label4.setToolTip("这是一个超链接")
        # 将4个label放置到垂直Layout当中
        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)    # 绑定槽函数

        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle("Qlabel控件演示")

    def linkHovered(self):
        print("当鼠标滑过Label2标签时，触发事件")

    def linkClicked(self):
        print("当鼠标单击label4时，触发事件")


if __name__ == '__main__' :
    app = QApplication(sys.argv)

    main = QLabelDemo()
    main.show()

    sys.exit(app.exec_())