# Form implementation generated from reading ui file 'D:\học đhoc\Hoc ky 2\Kỹ thuật lập trình\3nguoi\ui\Quanly\LoginQuanly\LoginQuanly.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 316)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\học đhoc\\Hoc ky 2\\Kỹ thuật lập trình\\3nguoi\\ui\\Quanly\\LoginQuanly\\../../../images/skibidi.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 121, 31))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(3, 110, 198);\n"
"border-radius: 10px;")
        self.label_2.setObjectName("label_2")
        self.IDlineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.IDlineEdit.setGeometry(QtCore.QRect(150, 110, 231, 31))
        self.IDlineEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.IDlineEdit.setText("")
        self.IDlineEdit.setObjectName("IDlineEdit")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(150, 160, 231, 31))
        self.lineEditPassword.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 121, 31))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(3, 110, 198);\n"
"border-radius: 10px;")
        self.label_3.setObjectName("label_3")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin.setGeometry(QtCore.QRect(160, 210, 111, 41))
        self.pushButtonLogin.setStyleSheet("QPushButton {\n"
"    /* Kiểu mặc định của nút */\n"
"background-color: #F0F8FF;\n"
"color: #048cfc;\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"border: 1px solid #048cfc;\n"
"}\n"
"\n"
"/* Khi di chuột qua nút */\n"
"QPushButton:hover {\n"
"    background-color: rgb(220, 236, 255);\n"
"}\n"
"\n"
"/* Khi nhấn nút */\n"
"QPushButton:pressed {\n"
"background-color: rgb(197, 227, 255);\n"
"    /* Bạn có thể thay đổi màu chữ, viền... nếu muốn */\n"
"}")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(-340, -420, 921, 821))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("D:\\học đhoc\\Hoc ky 2\\Kỹ thuật lập trình\\3nguoi\\ui\\Quanly\\LoginQuanly\\../../../images/backround.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.backbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(0, 0, 41, 28))
        self.backbutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\học đhoc\\Hoc ky 2\\Kỹ thuật lập trình\\3nguoi\\ui\\Quanly\\LoginQuanly\\../../../images/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backbutton.setIcon(icon1)
        self.backbutton.setObjectName("backbutton")
        self.HideAndOpenPass = QtWidgets.QPushButton(parent=self.centralwidget)
        self.HideAndOpenPass.setGeometry(QtCore.QRect(352, 160, 31, 31))
        self.HideAndOpenPass.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\học đhoc\\Hoc ky 2\\Kỹ thuật lập trình\\3nguoi\\ui\\Quanly\\LoginQuanly\\../../../images/ClosePassword.webp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.HideAndOpenPass.setIcon(icon2)
        self.HideAndOpenPass.setFlat(True)
        self.HideAndOpenPass.setObjectName("HideAndOpenPass")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 30, 261, 51))
        self.label.setStyleSheet("color: rgb(4, 140, 252);\n"
"border-radius: 15px;\n"
"padding: 5px;\n"
"background-color: rgb(211, 234, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"")
        self.label.setObjectName("label")
        self.label_10.raise_()
        self.label_2.raise_()
        self.IDlineEdit.raise_()
        self.lineEditPassword.raise_()
        self.label_3.raise_()
        self.pushButtonLogin.raise_()
        self.backbutton.raise_()
        self.HideAndOpenPass.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Skibidi Water"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ID:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Password:</p></body></html>"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:696; color:#048cfc;\">Login Screen</span></p></body></html>"))
