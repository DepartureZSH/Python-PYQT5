import sys
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.sound = QSound('pig.wav', self)              # 传入wav文件的路径来实例化一个QSound类
        self.sound.setLoops(QSound.Infinite)

        self.play_btn = QPushButton('Play Sound', self)
        self.stop_btn = QPushButton('Stop Sound', self)
        self.play_btn.clicked.connect(self.sound.play)
        self.stop_btn.clicked.connect(self.sound.stop)
        # 将按钮的信号和play()槽函数进行连接，这样每次点击按钮就会播放声音了

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.play_btn)
        self.h_layout.addWidget(self.stop_btn)
        self.setLayout(self.h_layout)
# Public Functions
#               QSound(const QString &filename, QObject *parent = Q_NULLPTR)
#               ~QSound()
# QString       fileName() const
# bool          isFinished() const
# int           loops() const
# int           loopsRemaining() const
# void          setLoops(int number)

# Public Slots
# void          play()
# void          stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
