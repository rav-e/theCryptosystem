# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TCT2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Text2(object):
    def setupUi(self, Text2):
        Text2.setObjectName("Text2")
        Text2.resize(746, 418)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        Text2.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Text2)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 50, 701, 111))
        self.plainTextEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 180, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 180, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 220, 701, 111))
        self.plainTextEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 340, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 340, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        Text2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Text2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Back = QtWidgets.QMenu(self.menubar)
        self.menu_Back.setObjectName("menu_Back")
        Text2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Text2)
        self.statusbar.setObjectName("statusbar")
        Text2.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_Back.menuAction())

        self.retranslateUi(Text2)
        QtCore.QMetaObject.connectSlotsByName(Text2)

    def retranslateUi(self, Text2):
        _translate = QtCore.QCoreApplication.translate
        Text2.setWindowTitle(_translate("Text2", "TheCryptosystem-Text2"))
        self.label.setText(_translate("Text2", "Type your Text "))
        self.pushButton.setText(_translate("Text2", "Encrypt"))
        self.pushButton_3.setText(_translate("Text2", "Decrypt"))
        self.pushButton_2.setText(_translate("Text2", "Copy"))
        self.pushButton_5.setText(_translate("Text2", "Clear All"))
        self.menu_Back.setTitle(_translate("Text2", "←Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Text2 = QtWidgets.QMainWindow()
    ui = Ui_Text2()
    ui.setupUi(Text2)
    Text2.show()
    sys.exit(app.exec_())
