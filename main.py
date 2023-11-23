from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QLabel, QPushButton, QFileDialog, QInputDialog
import sys
from pytube import YouTube


class Downloader(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(250, 250, 700, 210)
        self.setWindowTitle('скачиватель видео')
        self.line = QLineEdit(self)
        self.line.setGeometry(40, 50, 600, 20)

        self.text1 = QLabel(self)
        self.text1.setGeometry(40, 20, 300, 35)
        self.text1.setText('Здравствуйте! Введите в поле ниже ссылку на видео.')

        self.text2 = QLabel(self)
        self.text2.setGeometry(80, 120, 500, 35)
        self.text2.setText('')

        self.text3 = QLabel(self)
        self.text3.setGeometry(40, 120, 150, 35)
        self.text3.setText('Путь:')

        self.text4 = QLabel(self)
        self.text4.setGeometry(40, 140, 150, 35)
        self.text4.setText('Формат:')

        self.text5 = QLabel(self)
        self.text5.setGeometry(90, 140, 300, 35)

        self.text6 = QLabel(self)
        self.text6.setGeometry(40, 160, 150, 35)
        self.text6.setText('Качество:')

        self.text7 = QLabel(self)
        self.text7.setGeometry(100, 160, 150, 35)

        self.button = QPushButton(self)
        self.button.setGeometry(40, 80, 100, 30)
        self.button.setText('Установить путь')

        self.buttondownload = QPushButton(self)
        self.buttondownload.setGeometry(140, 80, 100, 30)
        self.buttondownload.setText('Скачать')

        self.button.clicked.connect(self.work)
        self.buttondownload.clicked.connect(self.work2)

    def work(self):
        wb_patch = QFileDialog.getExistingDirectory(self)
        self.text2.setText(wb_patch)
        format, ok_pressed = QInputDialog.getItem(
            self, "формат", "какой формат нужен?",
            ("mp3", "mp4"), 1, False)
        if ok_pressed and format:
            self.text5.setText(format)
        kachestvo, ok = QInputDialog.getItem(self, 'качество', 'какое качество желаете?', ('114', '123'), 1, False)
        if ok and kachestvo:
            self.text7.setText(kachestvo)

    def work2(self):
        self.myStream = YouTube(self.line.text()).streams.first()
        self.myStream.download(str(self.text2.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dw = Downloader()
    dw.show()
    sys.exit(app.exec())
