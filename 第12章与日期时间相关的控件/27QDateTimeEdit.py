# QDateTimeEdit是QDateEdit和QTimeEdit的父类
# QDateTimeEdit可以编辑日期和时间
# QDateEdit只能编辑日期(年月日)
# QTimeEdit只能编辑时间(时分秒)

import sys
from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QDateTimeEdit, QDateEdit, QTimeEdit, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.datetime_1 = QDateTimeEdit(self)                                                                # 实例化一个QDateTimeEdit控件1
        self.datetime_1.dateChanged.connect(lambda: print('Date Changed!'))     #连接信号dateChanged(日期改变)与槽函数print('Date Changed!')

        self.datetime_2 = QDateTimeEdit(QDateTime.currentDateTime(), self)       # 实例化一个QDateTimeEdit控件2，将日期时间设置为当前的日期和时间，默认2000/1/1 0:00 AM
        self.datetime_2.setDisplayFormat('yyyy-MM-dd HH:mm:ss')                         # setDisplayFormat()设置日期时间的显示格式
        self.datetime_2.timeChanged.connect(lambda: print('Time Changed!'))     #连接信号timeChanged(时间改变)与槽函数print('Time Changed!')
        print(self.datetime_2.date())
        print(self.datetime_2.time())
        print(self.datetime_2.dateTime())

        self.datetime_3 = QDateTimeEdit(QDateTime.currentDateTime(), self)          # 实例化一个QDateTimeEdit控件3，类似控件2
        self.datetime_3.dateTimeChanged.connect(lambda: print('DateTime Changed!'))  # 连接信号dateTimeChanged(日期或者时间改变)与槽函数print('Time Changed!')
        self.datetime_3.setCalendarPopup(True)                                                              # setCalendarPopup(True)设置日历弹窗

        self.datetime_4 = QDateTimeEdit(QDate.currentDate(), self)                      # self.datetime_4只传入了日期参数，没有时间
        self.datetime_5 = QDateTimeEdit(QTime.currentTime(), self)                     # self.datetime_5只传入了时间参数，没有日期

        self.date = QDateEdit(QDate.currentDate(), self)                                            # 实例化了一个QDateEdit控件，用法和QDateTimeEdit控件极为类似
        self.date.setDisplayFormat('yyyy/MM/dd')
        print(self.date.date())

        self.time = QTimeEdit(QTime.currentTime(), self)                                           # 实例化了一个QTimeEdit控件，用法和QDateTimeEdit控件极为类似
        self.time.setDisplayFormat('HH:mm:ss')
        print(self.time.time())

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.datetime_1)
        self.v_layout.addWidget(self.datetime_2)
        self.v_layout.addWidget(self.datetime_3)
        self.v_layout.addWidget(self.datetime_4)
        self.v_layout.addWidget(self.datetime_5)
        self.v_layout.addWidget(self.date)
        self.v_layout.addWidget(self.time)

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())