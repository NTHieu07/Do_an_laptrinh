# Form implementation generated from reading ui file 'D:\học đhoc\Hoc ky 2\Kỹ thuật lập trình\3nguoi\ui\Quanly\Giaodien\Quanly.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\học đhoc\\Hoc ky 2\\Kỹ thuật lập trình\\3nguoi\\ui\\Quanly\\Giaodien\\../../../images/skibidi.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 70, 361, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Nhansubutton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Nhansubutton.setFont(font)
        self.Nhansubutton.setStyleSheet("QPushButton {\n"
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
        self.Nhansubutton.setObjectName("Nhansubutton")
        self.verticalLayout.addWidget(self.Nhansubutton)
        self.Hoadonbutton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.Hoadonbutton.setStyleSheet("QPushButton {\n"
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
        self.Hoadonbutton.setObjectName("Hoadonbutton")
        self.verticalLayout.addWidget(self.Hoadonbutton)
        self.Menubutton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.Menubutton.setStyleSheet("QPushButton {\n"
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
        self.Menubutton.setObjectName("Menubutton")
        self.verticalLayout.addWidget(self.Menubutton)
        self.Thongkebutton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.Thongkebutton.setStyleSheet("QPushButton {\n"
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
        self.Thongkebutton.setObjectName("Thongkebutton")
        self.verticalLayout.addWidget(self.Thongkebutton)
        self.backbutton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(0, 0, 51, 31))
        self.backbutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\học đhoc\\Hoc ky 2\\Kỹ thuật lập trình\\3nguoi\\ui\\Quanly\\Giaodien\\../../../images/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.backbutton.setIcon(icon1)
        self.backbutton.setObjectName("backbutton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 811, 561))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.backbutton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Skibidi Water"))
        self.Nhansubutton.setText(_translate("MainWindow", "Nhân sự"))
        self.Hoadonbutton.setText(_translate("MainWindow", "Hóa đơn"))
        self.Menubutton.setText(_translate("MainWindow", "Menu"))
        self.Thongkebutton.setText(_translate("MainWindow", "Thống kê"))
