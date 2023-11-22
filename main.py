from PyQt5.QtWidgets import QApplication, QWidget
import sys


class Downloader(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 250, 700, 300)
        self.setWindowTitle('скачиватель видео')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dw = Downloader()
    dw.show()
    sys.exit(app.exec())
