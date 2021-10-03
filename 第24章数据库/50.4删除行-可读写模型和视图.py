import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
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
        model = QSqlTableModel()
        model.setTable('students')
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Class')
        model.setHeaderData(2, Qt.Horizontal, 'Name')
        model.setHeaderData(3, Qt.Horizontal, 'Score')

        model.insertRow(0)
        model.setData(model.index(0, 0), 2018010111)
        model.setData(model.index(0, 1), '0101')
        model.setData(model.index(0, 2), 'Who Cares')
        model.setData(model.index(0, 3), 0.5)
        model.submit()

        model.setFilter('score < 60')
        model.select()

        model.removeRow(0)  # 调用removeRow()方法传入索引值
        model.submit()

        self.setModel(model)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
