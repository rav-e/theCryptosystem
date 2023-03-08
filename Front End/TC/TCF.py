# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCF.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_File(object):
    def setupUi(self, File):
        File.setObjectName("File")
        File.resize(743, 415)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        File.setFont(font)
        self.centralwidget = QtWidgets.QWidget(File)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 80, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 90, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 240, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 160, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 80, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Sample again/upload.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        File.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(File)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 743, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Back = QtWidgets.QMenu(self.menubar)
        self.menu_Back.setObjectName("menu_Back")
        File.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(File)
        self.statusbar.setObjectName("statusbar")
        File.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_Back.menuAction())

        self.retranslateUi(File)
        QtCore.QMetaObject.connectSlotsByName(File)

    def retranslateUi(self, File):
        _translate = QtCore.QCoreApplication.translate
        File.setWindowTitle(_translate("File", "TheCryptosystem-File"))
        self.label.setToolTip(_translate("File", "<html><head/><body><p><span style=\" font-size:16pt;\">Upload File</span></p></body></html>"))
        self.label.setText(_translate("File", "Upload File:"))
        self.pushButton.setText(_translate("File", "Select"))
        self.pushButton_3.setText(_translate("File", "Decrypt"))
        self.pushButton_2.setText(_translate("File", "Encrypt"))
        self.menu_Back.setTitle(_translate("File", "←Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    File = QtWidgets.QMainWindow()
    ui = Ui_File()
    ui.setupUi(File)
    File.show()
    sys.exit(app.exec_())
