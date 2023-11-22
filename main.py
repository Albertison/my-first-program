from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QLabel, QPushButton
import sys
import pytube

class Downloader(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(250, 250, 700, 150)
        self.setWindowTitle('скачиватель видео')
        self.line = QLineEdit(self)
        self.line.setGeometry(40, 50, 600, 20)

        self.text1 = QLabel(self)
        self.text1.setGeometry(40, 20, 300, 35)
        self.text1.setText('Здравствуйте! Введите в поле ниже ссылку на видео.')

        self.button = QPushButton(self)
        self.button. setGeometry(40, 80, 100, 30)
        self.button.setText('Установить путь')

        self.buttondownload = QPushButton(self)
        self.buttondownload.setGeometry(140, 80, 100, 30)
        self.buttondownload.setText('Скачать')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dw = Downloader()
    dw.show()
    sys.exit(app.exec())
