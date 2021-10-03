import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.db = None
        self.db_connect()
        self.sql_exec()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('test_db')
        self.db.setUserName('root')
        self.db.setPassword('15828030238')
        if not self.db.open():
            QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

    def closeEvent(self, QCloseEvent):
        self.db.close()

    def sql_exec(self):
        query = QSqlQuery()
        # 实例化一个QSqlQuery对象，之后只用对该对象调用exec_()方法就可以执行SQL语句了
        query.exec_("CREATE TABLE students"  # 这里我们新建了一个students表，一共有四个字段id, class, name, score
                    "(id INT(11) PRIMARY KEY, class VARCHAR(4) NOT NULL, "
                    "name VARCHAR(25) NOT NULL, score FLOAT)")

        query.exec_("INSERT INTO students (id, class, name, score) "  # 这里插入两条数据。这里使用的是直接插入数据的方式
                    "VALUES (2018010401, '0104', 'Louis', 59.5)")
        query.exec_("INSERT INTO students (id, class, name, score) "
                    "VALUES (2018011603, '0116', 'Chris', 99.5)")
        # 还可以使用占位符进行插入，这时就需要用到prepare()方法
        # 首先是Oracle风格:
        # query.prepare("INSERT INTO students (id, class, name, score) "
        #                             "VALUES (:id, :class, :name, :score)")
        # query.bindValue(':id', 2018010401)
        # query.bindValue(':class', '0104')
        # query.bindValue(':name', 'Louis')
        # query.bindValue(':score', 59.5)
        # query.exec_()
        # 还有一种是ODBC风格:
        # query.prepare("INSERT INTO students (id, class, name, score) "
        #               "VALUES (?, ?, ?, ?)")
        # query.addBindValue(2018011603)
        # query.addBindValue('0116')
        # query.addBindValue('Chris')
        # query.addBindValue(99.5)
        # query.exec_()

        query.exec_("SELECT name, class, score FROM students")  # 进行查询操作
        # 调用next()方法就可以将记录指针定位到返回结果中的第一条
        # 调用value()方法传入相应的索引值就可以返回指定的字段数据
        while query.next():
            stu_name = query.value(0)
            stu_class = query.value(1)
            stu_score = query.value(2)
            print(stu_name, stu_class, stu_score)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
