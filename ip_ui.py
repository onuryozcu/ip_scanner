import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMenu, QAction
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


from ui_interface import *

import os
import socket
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow
class Main_Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main_Window, self).__init__(parent=parent)

        self.anapencere = Ui_MainWindow()
        self.anapencere.setupUi(self)

        self.anapencere.pushButton_2.clicked.connect(self.start_prog)
        self.anapencere.pushButton.clicked.connect(self.stop)

    def start_prog(self):

        x = self.ip_adress()
        y = self.first()
        z = self.last()

        net1 = x.split('.')
        a = '.'

        net2 = net1[0] + a + net1[1] + a + net1[2] + a
        st1 = int(y)
        en1 = int(z)
        en1 = en1 + 1
        t1 = datetime.now()

        self.run_system(st1,en1,net2)

    def scan(self,addr):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((addr, 135))
        if result == 0:
            return 1
        else:
            return 0

    def run_system(self,st1,en1,net2):
        for ip in range(st1, en1):
            addr = net2 + str(ip)
            if (self.scan(addr)):
                print(addr, "is live")

                rowPosition = self.anapencere.tableWidget.rowCount()
                self.anapencere.tableWidget.insertRow(rowPosition)

                # birinci parametresi satır ikinci parametresi sütun
                self.anapencere.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(addr))

    def ip_adress(self):
        ip = self.anapencere.lineEdit.text()
        return ip

    def first(self):
        first_ip = self.anapencere.lineEdit_1.text()
        return first_ip

    def last(self):
        last_ip = self.anapencere.lineEdit_2.text()
        return last_ip

    def stop(self):
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    pencere = Main_Window()
    pencere.show()

    sys.exit(app.exec_())