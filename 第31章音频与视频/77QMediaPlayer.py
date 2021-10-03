import sys
from PyQt5.Qt import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.player = QMediaPlayer(self)            # 实例化一个QMediaPlayer
        self.media_content = QMediaContent(QUrl.fromLocalFile('E:\python save\pyqt\practices\第31章音频与视频\媒体文件\MP3\music1.mp3'))  # 2
        # self.player.setMedia(QMediaContent(QUrl('http://example.com/music.mp3')))
        # 设置要播放的音频文件，首先要实例化一个QMediaContent类型的对象
        # 在实例化时要传入文件的路径(可以是本地文件，也可以是网络文件)
        self.player.setMedia(self.media_content)    # 之后该QMediaContent对象会作为参数传入setMedia()方法中
        self.player.setVolume(80)                   # 调用setVolume()来设置音量。
        # 100为默认值(最高音量)，传入0相当于静音
        self.player.play()                          # 调用play()方法播放音频文件


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())