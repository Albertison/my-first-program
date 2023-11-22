from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QLabel
import sys


class Downloader(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 250, 700, 300)
        self.setWindowTitle('скачиватель видео')
        self.line = QLineEdit(self)
        self.line.setGeometry(40, 50, 600, 20)

        self.text1 = QLabel(self)
        self.text1.setGeometry(40, 20, 300, 35)
        self.text1.setText('Здравствуйте! Введите в поле ниже ссылку на видео.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dw = Downloader()
    dw.show()
    sys.exit(app.exec())
