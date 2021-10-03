import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableView


class Demo(QTableView):
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
        model = QSqlQueryModel()            # 实例化一个QSqlQueryModel模型
        model.setQuery("SELECT id, name, class, score FROM students")   # 调用setQuery()方法来执行一个SQL查询语句
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        model.setHeaderData(2, Qt.Horizontal, 'Class')
        model.setHeaderData(3, Qt.Horizontal, ' Score')
        # setHeaderData()方法用来设置表格标题，若不使用该方法的话，程序则会默认使用数据表中的字段名作为标题

        self.setModel(model)                                    # 调用setModel()方法来设置视图所使用的模型
        # (注意这里程序直接继承QTableView，所以直接使用self)

        for i in range(model.rowCount()):               # 调用rowCount()方法获取行总数
            id = model.record(i).value('id')                # 将索引值传入record()中
            name = model.record(i).value(1)            # 并调用value()方法传入字段名(也可以传入索引)获取到id和name
            print(id, name)

        print('---------------------')

        for i in range(model.rowCount()):               # 还可以调用data()来获取数据,此时需要model.index的值
            id = model.data(model.index(i, 0))          # 调用index()传入行列索引值
            name = model.data(model.index(i, 1))
            print(id, name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())