import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import sys
import os


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 600, 600)
        self.setWindowTitle('Карта')

        self.inputX = QLineEdit('37.530822', self)
        self.inputX.move(60, 470)
        self.inputX.resize(85, 30)

        self.inputY = QLineEdit('2C55.702952', self)
        self.inputY.move(160, 470)
        self.inputY.resize(85, 30)

        self.inputZ = QLineEdit('15', self)
        self.inputZ.move(60, 530)
        self.inputZ.resize(100, 30)

        self.button_1 = QPushButton(self)
        self.button_1.move(180, 530)
        self.button_1.setText('Отобразить')
        self.button_1.clicked.connect(self.getImage)

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.getImage()

    def getImage(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.inputX.text()}%{self.inputY.text()}&z={self.inputZ.text()}&l=map"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap(self.map_file)
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_PageUp:
            self.inputZ.setText(str(int(self.inputZ.text()) + 1))
        if event.key() == QtCore.Qt.Key_PageDown:
            if int(self.inputZ.text()) != 0:
                self.inputZ.setText(str(int(self.inputZ.text()) - 1))
        self.getImage()
        event.accept()

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())