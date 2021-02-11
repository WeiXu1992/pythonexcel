'''
QLineEdit控件与回显模式

基本功能：输入单行文本
高级功能：设置回显模式

EchoMode(回显模式)
4种回显模式：
1，Normal
2，NoEcho，不回显模式
3，Password
4，PasswordEchoOnEdit

'''


from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QToolBox, QApplication, QPushButton, QWidget, QLabel

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本输入框的回显模式")

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoONEdit = QLineEdit()

        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("noEchoLineEdit", noEchoLineEdit)
        formLayout.addRow("passwordLineEdit", passwordLineEdit)
        formLayout.addRow("passwordEchoONEdit", passwordEchoONEdit)

        # placeholdertext
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("noEchoLineEdit")
        passwordLineEdit.setPlaceholderText("passwordLineEdit")
        passwordEchoONEdit.setPlaceholderText("passwordEchoONEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoONEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__' :
    app = QApplication(sys.argv)

    main = QLineEditEchoMode()
    main.show()

    sys.exit(app.exec_())