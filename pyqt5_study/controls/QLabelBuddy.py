'''
QLabel 与 伙伴控件

mainLayout.addWidget(控件对象，rowIndex , columnIndex , row , column)
'''

from PyQt5.QtWidgets import *
import sys


# from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QToolBox, QApplication, QPushButton, QWidget, QLabel

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()  # 易错问题点 super.__init__()    写法错误
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel与伙伴控件")

        namelabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        namelabel.setBuddy(nameLineEdit)

        passWorldLabel = QLabel('&passWord', self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passWorldLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(namelabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
        mainLayout.addWidget(passWorldLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)
        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)



if __name__ == '__main__' :
    app = QApplication(sys.argv)

    main = QLabelBuddy()
    main.show()

    sys.exit(app.exec_())