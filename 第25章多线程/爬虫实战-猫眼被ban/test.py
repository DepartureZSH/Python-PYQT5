import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSound
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import QThread, pyqtSignal, QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox,\
    QTextBrowser, QTableWidget, QTableWidgetItem, QHeaderView, QProgressBar,\
    QHBoxLayout, QVBoxLayout, QMessageBox

import json
import csv
import requests
from bs4 import BeautifulSoup

class CrawlWindow(QWidget):
    def __init__(self):
        super(CrawlWindow, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle("猫眼Top100电影爬取软件")
        self.setWindowIcon(QIcon('res/maoyan.png'))

        self.start_btn = QPushButton(self)
        self.stop_btn = QPushButton(self)
        self.save_combobox = QComboBox(self)
        self.table = QTableWidget(self)
        self.log_browser = QTextBrowser(self)
        self.progressbar = QProgressBar(self)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.crawl_thread = CrawlThread()
        self.db = None
        self.btn_sound = QSound('res/btn.wav', self)
        self.finish_sound = QSound('res/finish.wav', self)

        self.btn_init()
        self.combobox_init()
        self.table_init()
        self.progressbar_init()
        self.crawl_init()
        self.layout_init()

    def btn_init(self):
        self.start_btn.setText("开始爬取")
        self.stop_btn.setText("停止爬取")
        self.stop_btn.setEnabled(False)
        self.start_btn.clicked.connect(lambda: self.btn_slot(self.start_btn))
        self.stop_btn.clicked.connect(lambda : self.btn_slot(self.stop_btn))

    def combobox_init(self):
        save_list = ['另存到', 'MySQL', 'csv', 'txt', 'json']
        self.save_combobox.addItems(save_list)
        self.save_combobox.setEnabled(False)

        self.save_combobox.currentIndexChanged.connect(self.combobox_slot)

    def table_init(self):
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['图片链接', '电影名称', '主演人员', '上映时间', '电影评分'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def progressbar_init(self):
        self.progressbar.setRange(0, 100)
        self.progressbar.setValue(0)

    def layout_init(self):
        self.h_layout.addWidget(self.start_btn)
        self.h_layout.addWidget(self.stop_btn)
        self.h_layout.addWidget(self.save_combobox)
        self.v_layout.addWidget(self.table)
        self.v_layout.addWidget(self.log_browser)
        self.v_layout.addWidget(self.progressbar)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def crawl_init(self):
        self.crawl_thread.finished_signal.connect(self.finish_slot)
        self.crawl_thread.log_signal.connect(self.set_log_slot)
        self.crawl_thread.result_signal.connect(self.set_table_slot)

    def finish_slot(self):
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.save_combobox.setEnabled(True)

    def set_log_slot(self, new_log):
        self.log_browser.append(new_log)

    def set_table_slot(self, img, name, star, time, score):
        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(img))
        self.table.setItem(row, 1, QTableWidgetItem(name))
        self.table.setItem(row, 2, QTableWidgetItem(star))
        self.table.setItem(row, 3, QTableWidgetItem(time))
        self.table.setItem(row, 4, QTableWidgetItem(score))

        self.progressbar.setValue(row+1)
        if self.progressbar.value() == 100:
            self.finish_sound.play()

    def btn_slot(self, btn):
        self.btn_sound.play()
        if btn == self.start_btn:
            self.log_browser.clear()
            self.log_browser.append('<font color="red">开始爬取</font>')
            self.table.clearContents()
            self.table.setRowCount(0)
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.save_combobox.setEnabled(False)

            self.crawl_thread.start()
        else:
            self.log_browser.append('<font color="red">停止爬取</font>')
            self.stop_btn.setEnabled(False)
            self.start_btn.setEnabled(True)
            self.save_combobox.setEnabled(True)

            self.crawl_thread.terminate()

    def combobox_slot(self, text):
        if text == 'MySQL':
            self.save_to_MySQL()
        elif text == 'csv':
            self.save_to_csv()
        elif text == 'txt':
            self.save_to_txt()
        else:
            self.save_to_json()

    def save_to_MySQL(self):
        query = QSqlQuery()
        query.exec_("create table if not exists movie"
                    "(img varchar(100), name varchar(50), star varchar(100),"
                    " time varchar(50), score varchar(5))")
        for row in range(self.table.rowCount()):
            img = self.table.item(row, 0).text()
            name = self.table.item(row, 1).text()
            star = self.table.item(row, 2).text()
            time = self.table.item(row, 3).text()
            score = self.table.item(row, 4).text()
        query.prepare("insert into movie (img,name,star,time,score)"
                      "values(?,?,?,?,?)")
        query.addBindValue(img)
        query.addBindValue(name)
        query.addBindValue(star)
        query.addBindValue(time)
        query.addBindValue(score)
        query.exec_()
        QMessageBox.information(self, '保存到MySQL', '保存成功!', QMessageBox.Ok)

    def save_to_csv(self):
        content = []
        for row in range(self.table.rowCount()):
            img = self.table.item(row, 0).text()
            name = self.table.item(row, 1).text()
            star = self.table.item(row, 2).text()
            time = self.table.item(row, 3).text()
            score = self.table.item(row, 4).text()
            content.append([img, name, star, time, score])

        with open('./猫眼Top100电影.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['图片链接', '电影名称', '主演人员', '上映时间', '电影评分'])
            writer.writerows(content)
        QMessageBox.information(self, '保存到csv', '保存成功!', QMessageBox.Ok)

    def save_to_txt(self):
        content = ''
        for row in range(self.table.rowCount()):
            img = '图片链接：{}\n'.format(self.table.item(row, 0).text())
            name = '电影名称：{}\n'.format(self.table.item(row, 1).text())
            star = '主演人员：{}\n'.format(self.table.item(row, 2).text())
            time = '上映时间：{}\n'.format(self.table.item(row, 3).text())
            score = '电影评分：{}\n'.format(self.table.item(row, 4).text())
            content += img + name + star + time + score + '\n'

        with open('./猫眼Top100电影.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        QMessageBox.information(self, '保存到txt', '保存成功!', QMessageBox.Ok)

    def save_to_json(self):
        content = []
        for row in range(self.table.rowCount()):
            img = self.table.item(row, 0).text()
            name = self.table.item(row, 1).text()
            star = self.table.item(row, 2).text()
            time = self.table.item(row, 3).text()
            score = self.table.item(row, 4).text()
            content.append(
                {
                    '图片链接': img,
                    '电影名称': name,
                    '主演人员': star,
                    '上映时间': time,
                    '电影评分': score
                }
            )
            with open('./猫眼Top100电影.json', 'w', encoding='utf-8') as f:
                json.dump(content, f, ensure_ascii=False)
            QMessageBox.information(self, '保存到json', '保存成功!', QMessageBox.Ok)

    def closeEvent(self, QCloseEvent):
        self.db.close()

class CrawlThread(QThread):
    finished_signal = pyqtSignal()
    log_signal = pyqtSignal(str)
    result_signal = pyqtSignal(str, str, str, str, str)

    def __init__(self):
        super(CrawlThread, self).__init__()

    def get_page(self, url):
        try:
            headers = {
                "UserAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.text
            else:
                self.log_signal.emit(" 状态吗返回错误，请求失败")
                return None
        except Exception as e:
            self.log_signal.emit(e)
            return None

    def parse_page(self, html):
        soup = BeautifulSoup(html, features='lxml')
        img_list = [s.get('data-src') for s in soup.select('dd img.board-img')]
        name_list = [s.text for s in soup.select('p.name>a')]
        star_list = [s.text.strip().split(': ')[-1] for s in soup.select('p.star')]
        time_list = [s.text.strip().split(': ')[-1] for s in soup.select('p.releasetime')]
        score_list = [s.text for s in soup.select('p.score')]

        for i in range(10):
            self.result_signal.emit(img_list[i], name_list[i], star_list[i], time_list[i], score_list[i])

    def run(self):
        base_url = "https://maoyan.com/board/4?offset={}"
        for i in range(10):
            self.log_signal.emit("开始爬取第{}页".format(i + 1))
            url = base_url.format(i * 10)
            html = get_page(url)
            parse_page(html)

        self.log_signal.emit('全部爬取完毕！')
        self.finished_signal.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = CrawlWindow()
    demo.show()
    sys.exit(app.exec_())
