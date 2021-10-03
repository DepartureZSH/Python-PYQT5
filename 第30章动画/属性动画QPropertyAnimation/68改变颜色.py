import sys
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

# 由于按钮并没有颜色属性color，所以我们不能单纯的将b'color'传入，必须要创建一个
# 注意属性必须要有一个设置函数[setter]，即属性可写，才可以在动画中起效果
# 如：pos和geometry属性 对应 setGeometry()函数
#              size属性 对应 resize()函数

# 第一种方法：
# @property装饰器：
# 可以将一个方法转换为具有相同名称的只读属性，其实就是加了一个我们需要的属性
# pyqt5中@pyqtProperty()：
class MyButton(QPushButton):
    def __init__(self, text=None, parent=None):
        super(MyButton, self).__init__(text, parent)
        self._color = QColor()

    @pyqtProperty(QColor)       # 通过@pyqtproperty装饰器创建了一个QColor属性
    def color(self):
        return self._color

    @color.setter               # 通过@color.setter装饰器给该属性一个设置函数
    def color(self, col):
        self._color = col
        self.setStyleSheet('background-color: rgb({}, {}, {})'.format(col.red(), col.green(), col.blue()))

# # 第二种方法：
# # property()函数（python）
# # 该函数的作用是返回属性值
# # 在pyqt5中pyqtProperty()：
# class MyButton(QPushButton):
#     def __init__(self, text=None, parent=None):
#         super(MyButton, self).__init__(text, parent)
#         self._color = QColor()
#
#     def get_color(self):
#         return self._color
#
#     def set_color(self, col):
#         self._color = col
#         self.setStyleSheet('background-color: rgb({}, {}, {})'.format(col.red(), col.green(), col.blue()))
#
#     color = pyqtProperty(QColor, fget=get_color, fset=set_color)
#     # pyqtProperty()的第一个参数要填属性类型，其他参数和python的property()函数一样：
#     # property()函数中的fget参数为用于读取属性值的函数，
#     # 而fset是用于设置属性值的函数。
#     # 返回属性值保存在color中，也就是我们自定义的属性。

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.btn = MyButton('Color', self)
        self.btn.setGeometry(0, 0, 100, 100)

        self.animation = QPropertyAnimation(self.btn, b'color')
        self.animation.setDuration(5000)
        # 让颜色用rgb(0, 0, 0)变换到rgb(255, 255, 255)，即黑到白
        self.animation.setStartValue(QColor(0, 0, 0))
        self.animation.setEndValue(QColor(255, 255, 255))
        self.animation.setLoopCount(-1)
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
