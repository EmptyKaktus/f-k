import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
import sys
import os

geocoder_request = "https://static-maps.yandex.ru/1.x/?ll=133.251106%2C-29.603809&spn=22,22&l=map"
response = requests.get(geocoder_request)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 600, 600)
        self.setWindowTitle('Карта')

        self.pixmap = QPixmap(map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def map(self):
        pass

    def coor(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

os.remove(map_file)