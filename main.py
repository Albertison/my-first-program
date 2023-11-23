import sys
import threading

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QLabel, QPushButton, QFileDialog
from pytube import YouTube


class Downloader(QWidget):
    wt: YouTube

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
        self.text5.setText('mp4')

        self.text6 = QLabel(self)
        self.text6.setGeometry(40, 160, 150, 35)
        self.text6.setText('Качество:')

        self.text7 = QLabel(self)
        self.text7.setGeometry(100, 160, 150, 35)
        self.text7.setText('высшее по умолчанию')

        self.button = QPushButton(self)
        self.button.setGeometry(40, 80, 100, 30)
        self.button.setText('Установить путь')

        self.buttondownload = QPushButton(self)
        self.buttondownload.setGeometry(140, 80, 100, 30)
        self.buttondownload.setText('Скачать')

        self.button.clicked.connect(self.work)
        self.buttondownload.clicked.connect(self.thread_process)

    def work(self):
        wb_patch = QFileDialog.getExistingDirectory(self)
        self.text2.setText(wb_patch)

    def work2(self):
        link = self.line.text()
        self.wt = YouTube(link)
        ws = self.wt.streams.get_highest_resolution()
        ws.download(self.text2.text())
        print('end')

    def thread_process(self):
        thread = threading.Thread(target=self.work2)
        thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dw = Downloader()
    dw.show()
    sys.exit(app.exec())
