import sys
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel, QVBoxLayout

EMOTION = {                                                    # 设置一个字典，并将各个星期(中英文系统的key不同)及对应的颜文字分别作为键值输入
    '周一': '(╯°Д°)╯︵ ┻━┻',
    '周二': '(╯￣Д￣)╯╘═╛',
    '周三': '╭(￣▽￣)╯╧═╧',
    '周四': '_(:з」∠)_',
    '周五': '(๑•̀ㅂ•́) ✧',
    '周六': '( ˘ 3˘)♥',
    '周日': '(;′༎ຶД༎ຶ`)'
}


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.calendar = QCalendarWidget(self)
        self.calendar.setMinimumDate(QDate(1946, 2, 14))                                # setMinimumDate()设置日历的最小日期
        self.calendar.setMaximumDate(QDate(6666, 6, 6))                                 # setMaximumDate()设置日历的最大日期
        # self.calendar.setDateRange(QDate(1946, 2, 14), QDate(6666, 6, 6)) # setDateRange()设置日历的日期范围
        # self.calendar.setFirstDayOfWeek(Qt.Monday)                          # setFirstDayOfWeek()设置一个星期的第一天，默认第一天为星期天
        # self.calendar.setSelectedDate(QDate(1946, 2, 14))                   # setSelectedDate()设置日历初始化时所显示的日期，默认是当天日期
        self.calendar.setGridVisible(False)                                                    # setGridVisible(bool)设置是否在日历上显示网格

        self.calendar.clicked.connect(self.show_emotion_func)            # 连接信号clicked(点击到日历上的某个日期)与槽函数show_emotion_func()

        print(self.calendar.minimumDate())                                               # minimumDate()获取日历的最早日期，类型为QDate
        print(self.calendar.maximumDate())                                              # maximumDate()获取日历的最后日期，类型为QDate
        print(self.calendar.selectedDate())                                                  # selectedDate()获取日历的当前所选日期，类型为QDate

        self.label = QLabel(self)                                                                      # 实例化一个QLabel控件，显示颜文字
        self.label.setAlignment(Qt.AlignCenter)

        weekday = self.calendar.selectedDate().toString('ddd')              # toString(‘ddd‘)获取星期的缩写，然后作为字典的键获取对应的值
        self.label.setText(EMOTION[weekday])

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.calendar)
        self.v_layout.addWidget(self.label)

        self.setLayout(self.v_layout)
        self.setWindowTitle('QCalendarWidget')

    def show_emotion_func(self):                                                             # toString(‘ddd‘)获取星期的缩写，然后作为字典的键获取对应的值
        weekday = self.calendar.selectedDate().toString('ddd')
        self.label.setText(EMOTION[weekday])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())