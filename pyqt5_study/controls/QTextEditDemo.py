'''
QTextEdit控件
'''

from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit控件演示')

        self.resize(300, 500)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton('显示文本')
        self.buttonHtml = QPushButton('显示Html')

        self.buttonToText = QPushButton('获取文本')
        self.buttonToHtml = QPushButton('获取Html')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonHtml)
        layout.addWidget(self.buttonToHtml)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.OnClick_ButtonText)
        self.buttonHtml.clicked.connect(self.OnClick_ButtonHtml)

        self.buttonToText.clicked.connect(self.OnClick_ButtonToText)
        self.buttonToHtml.clicked.connect(self.OnClick_ButtonToHtml)

    def OnClick_ButtonText(self):
        self.textEdit.setPlainText('hello World, 你好么世界？')

    def OnClick_ButtonToText(self):
        print(self.textEdit.toPlainText())

    def OnClick_ButtonHtml(self):
        self.textEdit.setHtml('<font color="blue" size="25">hello World</font>')

    def OnClick_ButtonToHtml(self):
        print(self.textEdit.toHtml())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())