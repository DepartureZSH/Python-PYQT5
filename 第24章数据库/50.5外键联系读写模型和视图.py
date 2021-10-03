import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableView


class Demo(QTableView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 200)
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
        model = QSqlRelationalTableModel()
        model.setTable('students')

        # 建立表之间的联系
        # 调用setRelation()方法。传入两个参数，第一个是作为外键的索引，第二个是QSqlRelation对象
        # 1、这里把class字段作为外键的，而在students表中class外键的索引为1
        # 2、QSqlRelation对象实例化需要三个参数：外键关系对应的表、外键字段名 以及 要进行显示的字段
        # （1）外键关系对应的表 很明显就是teachers
        # （2）teachers表中主键名class就是联系时用的 外键字段名
        # （3）最后teachers中的name字段就是 要显示的字段

        # 简单来说，这行代码就是把两个表建立了联系
        # 并且把students中class字段下的值换成teachers表中name字段下的值用于显示
        model.setRelation(1, QSqlRelation('teachers', 'class', 'name'))

        # 设置表格标题，因为显示的不是班级而是老师的名字，所以把Class改成了Teacher
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Teacher')
        model.setHeaderData(2, Qt.Horizontal, 'Student')
        model.setHeaderData(3, Qt.Horizontal, 'Score')
        model.select()

        self.setModel(model)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
