import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QCheckBox, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.sound_effect = QSoundEffect(self)                   # 实例化QSoundEffect类
        self.sound_effect.setSource(QUrl.fromLocalFile('sound.wav'))  # 调用setSource()来设置音频源
        # 需要传入QUrl类型参数
        self.sound_effect.setVolume(1.0)                         # setVolume()设置播放音频时的音量大小
        # 参数为浮点型数值。1.0代表全音量播放，0.0代表静音
        self.play_btn = QPushButton('Play Sound', self)
        self.play_btn.clicked.connect(self.sound_effect.play)

        self.slider = QSlider(Qt.Horizontal, self)                      # 实例化QSlider滑动条控件
        self.slider.setRange(0, 10)
        self.slider.setValue(10)
        self.slider.valueChanged.connect(self.set_volume_func)

        self.checkbox = QCheckBox('Mute', self)                         # 实例化QCheckBox复选框
        # 此复选框控制是否需要静音
        self.checkbox.stateChanged.connect(self.mute_func)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h_layout.addWidget(self.play_btn)
        self.h_layout.addWidget(self.checkbox)
        self.v_layout.addWidget(self.slider)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def set_volume_func(self):
        self.sound_effect.setVolume(self.slider.value()/10)
    # 将滑动条的当前数值除以10来获取到一个浮点型数值
    # 将该数值作为setVolume()方法的参数

    def mute_func(self):
        if self.sound_effect.isMuted():                     # 先用isMuted()方法判断当前是否已经静音
            self.sound_effect.setMuted(False)
        else:
            self.sound_effect.setMuted(True)                # 没静音则调用setMute()方法设置静音


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())