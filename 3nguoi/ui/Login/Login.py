# Form implementation generated from reading ui file 'D:\học đhoc\Hoc ky 2\Kỹ thuật lập trình\3nguoi\ui\Login\Login.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 424)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\học đhoc\\Hoc ky 2\\Kỹ thuật lập trình\\3nguoi\\ui\\Login\\../../images/skibidi.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #F0F8FF;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 451, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.label_2.setStyleSheet("color: rgb(4, 140, 252);\n"
"border-radius: 15px;\n"
"padding: 5px;\n"
"background-color: #D0E1F9;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 120, 421, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #048cfc;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.quanlybutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.quanlybutton.setGeometry(QtCore.QRect(380, 270, 221, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.quanlybutton.setFont(font)
        self.quanlybutton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.quanlybutton.setStyleSheet("QPushButton {\n"
"    /* Kiểu mặc định của nút */\n"
"background-color: #F0F8FF;\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: #048cfc;\n"
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
        self.quanlybutton.setAutoDefault(False)
        self.quanlybutton.setObjectName("quanlybutton")
        self.khachhangbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.khachhangbutton.setGeometry(QtCore.QRect(380, 190, 221, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.khachhangbutton.setFont(font)
        self.khachhangbutton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.khachhangbutton.setStyleSheet("QPushButton {\n"
"    /* Kiểu mặc định của nút */\n"
"background-color: #F0F8FF;\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: #048cfc;\n"
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
        self.khachhangbutton.setObjectName("khachhangbutton")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(0, -30, 771, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("D:\\học đhoc\\Hoc ky 2\\Kỹ thuật lập trình\\3nguoi\\ui\\Login\\../../images/backround.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_10.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.quanlybutton.raise_()
        self.khachhangbutton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Skibidi Water"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">ĐĂNG NHẬP HỆ THỐNG</span></p></body></html>"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Hãy chọn vai trò của bạn để tiếp tục!</p></body></html>"))
        self.quanlybutton.setText(_translate("MainWindow", "Quản lý"))
        self.khachhangbutton.setText(_translate("MainWindow", "Khách hàng"))
