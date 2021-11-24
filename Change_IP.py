from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess as sp
import time
def reconnect_app(name_dcom):
    sp.call('rasdial /disconnect')
    time.sleep(5)
    sp.call('rasdial '+name_dcom)
    time.sleep(5)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Change_IP = QtWidgets.QPushButton(self.centralwidget)
        self.Change_IP.setGeometry(QtCore.QRect(290, 10, 101, 41))
        self.Change_IP.setObjectName("Change_IP")
        self.Dcom_name = QtWidgets.QLineEdit(self.centralwidget)
        self.Dcom_name.setGeometry(QtCore.QRect(130, 20, 141, 20))
        self.Dcom_name.setObjectName("Dcom_name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Change_IP.clicked.connect(self.CP_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Change_IP.setText(_translate("MainWindow", "Change_IP"))
        self.label.setText(_translate("MainWindow", "Dcom_Name"))
    def CP_clicked(self):
        reconnect_app(name_dcom=self.Dcom_name.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
