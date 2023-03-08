# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCT1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#importing Text2 window
from TCT2 import Ui_Text2

class Ui_Text(object):
    def setupUi(self, Text):
        Text.setObjectName("Text")
        Text.resize(751, 424)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        Text.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Text)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 150, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(390, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Sample again/BABY_ICONS_COLOR-01-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Sample again/download-removebg-preview (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Sample again/Incognitologo_square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 350, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        Text.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Text)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Back = QtWidgets.QMenu(self.menubar)
        self.menu_Back.setObjectName("menu_Back")
        Text.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Text)
        self.statusbar.setObjectName("statusbar")
        Text.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_Back.menuAction())

        self.retranslateUi(Text)
        QtCore.QMetaObject.connectSlotsByName(Text)
        self.pushButton.clicked.connect(self.secondt)
    def secondt(self):
        #code for secondt
        self.Text2 = QtWidgets.QMainWindow()
        self.ui = Ui_Text2()
        self.ui.setupUi(self.Text2)
        self.Text2.show()

    def retranslateUi(self, Text):
        _translate = QtCore.QCoreApplication.translate
        Text.setWindowTitle(_translate("Text", "TheCryptosystem-Text"))
        self.label_2.setToolTip(_translate("Text", "<html><head/><body><p><span style=\" font-size:16pt;\">Upload File</span></p></body></html>"))
        self.label_2.setText(_translate("Text", "Protection Levl:"))
        self.comboBox.setItemText(0, _translate("Text", "Script Kidde"))
        self.comboBox.setItemText(1, _translate("Text", "Programmer"))
        self.comboBox.setItemText(2, _translate("Text", "Black Hat"))
        self.pushButton.setText(_translate("Text", "Next"))
        self.menu_Back.setTitle(_translate("Text", "←Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Text = QtWidgets.QMainWindow()
    ui = Ui_Text()
    ui.setupUi(Text)
    Text.show()
    sys.exit(app.exec_())
