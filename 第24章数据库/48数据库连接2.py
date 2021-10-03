import sys
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.db = None
        self.db_connect()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')     # 要连接MySQL数据库那就要使用QMYSQL驱动
        self.db.setHostName('localhost')                 # 调用setHostName()方法设置主机名，因为是本地的，所以直接写localhost
        self.db.setDatabaseName('test_db')               # 调用setDatabaseName()设置要使用的(已存在)数据库名称
        self.db.setUserName('root')                      # 调用setUserName()和setPassword()来分别输入数据库的用户名和密码
        self.db.setPassword('15828030238')                    # 5
        if not self.db.open():
            QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

    def closeEvent(self, QCloseEvent):
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())