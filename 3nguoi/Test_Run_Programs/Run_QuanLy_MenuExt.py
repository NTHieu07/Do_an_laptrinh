
import sys
from PyQt6.QtWidgets import QApplication

from ui.Quanly.QuanLyMenu.MenuExt import MenuExt

app = QApplication(sys.argv)
window = MenuExt()
window.show()
sys.exit(app.exec())
