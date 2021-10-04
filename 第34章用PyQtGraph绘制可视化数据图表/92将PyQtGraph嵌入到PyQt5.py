import sys
import random
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        # 进行全局设置：禁止拖动、背景色为白色、前景色为黑色；
        pg.setConfigOptions(leftButtonPan=False)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        # 利用NumPy库生成高斯分布的概率密度随机数作为x轴和y轴坐标数据，并随机挑选符号以及颜色
        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        r_symbol = random.choice(['o', 's', 't', 't1', 't2', 't3', 'd', '+', 'x', 'p', 'h', 'star'])
        r_color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's'])

        # 实例化一个PlotWidget对象
        self.pw = pg.PlotWidget(self)
        # pyqtgraph.plot绘制图表：无画笔、坐标点符号为r_symbol、符号画刷颜色为r_color
        # 返回一个PlotDataItem对象存储在self.new_plot变量中(该对象就是图表上的数据整体)
        self.plot_data = self.pw.plot(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)

        # 按钮用于重新绘制数据
        self.plot_btn = QPushButton('Replot', self)
        # 在槽函数中调用setData()方法重新设置数据
        # (如果我们在槽函数中调用self.pw.plot()的话，那新数据就会被重叠绘制到旧数据上)
        self.plot_btn.clicked.connect(self.plot_slot)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.pw)
        self.v_layout.addWidget(self.plot_btn)
        self.setLayout(self.v_layout)

    def plot_slot(self):
        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        r_symbol = random.choice(['o', 's', 't', 't1', 't2', 't3', 'd', '+', 'x', 'p', 'h', 'star'])
        r_color = random.choice(['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's'])
        self.plot_data.setData(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
