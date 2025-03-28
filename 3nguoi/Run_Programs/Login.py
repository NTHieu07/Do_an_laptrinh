from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.Login.LoginExt import LoginExt

app = QApplication([])
MainWindow = QMainWindow()
myui = LoginExt()
myui.setupUi(MainWindow)
myui.show()
app.exec()