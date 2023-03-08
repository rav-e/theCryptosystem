# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TC.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#importing file Screen
from TCF import Ui_File

#importing text Screen
from TCT1 import Ui_Text

class Ui_TheCryptosystem(object):
    def setupUi(self, TheCryptosystem):
        TheCryptosystem.setObjectName("TheCryptosystem")
        TheCryptosystem.resize(740, 411)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        TheCryptosystem.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../2_lQHUBEQe3GmKJdbAxKRFig-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TheCryptosystem.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TheCryptosystem)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(250, 170, 71, 71))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(500500, 50000))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Interface/samples/Sample again/file_document-text-note-txt-512.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(410, 170, 81, 81))
        self.label_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Sample again/file-explorer-folder-libraries-icon-18298.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 170, 71, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Sample again/file_document-text-note-txt-512.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        TheCryptosystem.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TheCryptosystem)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 21))
        self.menubar.setObjectName("menubar")
        TheCryptosystem.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TheCryptosystem)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(8)
        self.statusbar.setFont(font)
        self.statusbar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusbar.setObjectName("statusbar")
        TheCryptosystem.setStatusBar(self.statusbar)

        self.retranslateUi(TheCryptosystem)
        QtCore.QMetaObject.connectSlotsByName(TheCryptosystem)
        self.pushButton.clicked.connect(self.textscr)
    def textscr(self):
        #Text screen code
        self.Text = QtWidgets.QMainWindow()
        self.ui = Ui_Text()
        self.ui.setupUi(self.Text)
        self.Text.show()

        self.pushButton_2.clicked.connect(self.filescr)
    def filescr(self):
        #file screen code
        self.File = QtWidgets.QMainWindow()
        self.ui = Ui_File()
        self.ui.setupUi(self.File)
        self.File.show()

        
        

    def retranslateUi(self, TheCryptosystem):
        _translate = QtCore.QCoreApplication.translate
        TheCryptosystem.setWindowTitle(_translate("TheCryptosystem", "TheCryptosystem"))
        self.pushButton.setText(_translate("TheCryptosystem", "Text"))
        self.pushButton_2.setText(_translate("TheCryptosystem", "File"))
        self.label.setText(_translate("TheCryptosystem", "<html><head/><body><p><span style=\" font-size:28pt; color:#ff0000;\">T</span><span style=\" font-size:28pt;\">he</span><span style=\" font-size:28pt; color:#ff0000;\">C</span><span style=\" font-size:28pt;\">ryptosystem</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TheCryptosystem = QtWidgets.QMainWindow()
    ui = Ui_TheCryptosystem()
    ui.setupUi(TheCryptosystem)
    TheCryptosystem.show()
    sys.exit(app.exec_())
