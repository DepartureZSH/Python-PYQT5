import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Demo(QWidget):                                            # 继承QWidget类
    def __init__(self):
        super(Demo, self).__init__()                                #QWidget类init方法初始化
        self.button = QPushButton('Start', self)                # 创造一个button
        self.button.clicked.connect(self.change_text)           # 连接connect信号clicked(按钮被点击)与槽函数self.change_text

    def change_text(self):
        print('change text')
        self.button.setText('Stop')                             # 改变button
        self.button.clicked.disconnect(self.change_text)        # 解绑disconnect信号clicked(按钮被点击)和槽函数self.change_text

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()                                               # 实例化Demo类
    demo.show()                                                 # 使demo可见
    sys.exit(app.exec_())