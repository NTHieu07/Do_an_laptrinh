import os
import matplotlib.pyplot as plt
import xlsxwriter
from PyQt6 import QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime
from collections import defaultdict
from PyQt6.QtWidgets import QVBoxLayout, QMainWindow, QMessageBox, QFileDialog
from ui.Quanly.ThongKeWindow.thongke import Ui_MainWindow  # file thongke.ui chuyển thành Ui_MainWindow
from libs.Dataconnector import DataConnector

class ThongkeExt(Ui_MainWindow):
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.background = os.path.join(current_dir, "..", "..", "..", "images", "backround.png")
        self.back = os.path.join(current_dir, "..", "..", "..", "images", "back.png")
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.data_connector = DataConnector()
        self.label_4.setPixmap(QtGui.QPixmap(self.background))
        self.HomeButton.setIcon(QtGui.QIcon(self.back))
        # Kết nối các signal để tự động vẽ lại đồ thị khi thay đổi điều kiện
        self.LoaiDonHangcombobox.currentIndexChanged.connect(self.plot_thongke)
        self.comboBoxhinhthuc.currentIndexChanged.connect(self.plot_thongke)
        self.StarttimeEdit.dateChanged.connect(self.plot_thongke)
        self.EndtimeEdit.dateChanged.connect(self.plot_thongke)
        self.HomeButton.clicked.connect(self.Home)
        self.actionExport_to_Excel.triggered.connect(self.export_to_excel)
        self.plot_thongke()

    def plot_thongke(self):
        # Lấy thời gian bắt đầu và kết thúc (QDate -> datetime.date)
        start_date = self.StarttimeEdit.date().toPyDate()
        end_date = self.EndtimeEdit.date().toPyDate()

        # Lấy danh sách đơn hàng và lọc theo thời gian
        orders = self.data_connector.get_all_orders()
        filtered_orders = []
        for order in orders:
            try:
                dt = datetime.strptime(order.time, "%d-%m-%Y %H:%M:%S")
            except Exception:
                continue
            if start_date <= dt.date() <= end_date:
                filtered_orders.append(order)

        # Lọc theo loại đơn hàng nếu cần (không phải "tất cả")
        loai_don = self.LoaiDonHangcombobox.currentText().strip().lower()
        if loai_don != "tất cả":
            tokens = loai_don.split()  # tách thành các token, vd: ["nước", "ép"]
            temp = []
            for order in filtered_orders:
                found = False
                for prod in order.products:
                    # Luôn lấy tên sản phẩm là phần trước dấu ":" (đảm bảo nhất quán)
                    name_part = prod.split(":")[0].strip().lower()
                    words = name_part.split()
                    if all(token in words for token in tokens):
                        found = True
                        break
                if found:
                    temp.append(order)
            filtered_orders = temp

        # Xác định cách nhóm thời gian dựa trên khoảng cách
        delta = (end_date - start_date).days
        if delta <= 7:
            group_by = "day"
        elif delta <= 31:
            group_by = "day"  # hoặc nhóm theo tuần nếu cần
        elif delta <= 366:
            group_by = "month"
        else:
            group_by = "year"

        revenue = defaultdict(float)  # Tổng thu nhập theo nhóm thời gian (cho "Tổng quan")
        detail = defaultdict(lambda: defaultdict(float))  # detail[group][product_name] = doanh thu

        mode = self.comboBoxhinhthuc.currentText().strip().lower()  # "tổng quan" hoặc "chi tiết"

        # Duyệt qua từng đơn hàng 1 lần
        for order in filtered_orders:
            try:
                dt = datetime.strptime(order.time, "%d-%m-%Y %H:%M:%S")
            except Exception:
                continue

            # Xác định key nhóm theo thời gian
            if group_by == "day":
                key = dt.strftime("%d-%m-%Y")
            elif group_by == "month":
                key = dt.strftime("%m-%Y")
            elif group_by == "year":
                key = dt.strftime("%Y")
            else:
                key = dt.strftime("%d-%m-%Y")

            revenue[key] += order.totalprice

            if mode == "chi tiết":
                # Nếu loai_don không phải "tất cả", ta sẽ chỉ thêm những sản phẩm thỏa mãn token
                tokens_filter = None
                if loai_don != "tất cả":
                    tokens_filter = loai_don.split()
                for prod in order.products:
                    # Lấy tên sản phẩm theo cách nhất quán
                    name_part = prod.split(":")[0].strip()
                    try:
                        prod_price = float(prod.split(":")[-1].strip())
                    except Exception:
                        prod_price = 0

                    if tokens_filter is None:
                        detail[key][name_part] += prod_price
                    else:
                        words = name_part.lower().split()
                        if all(token in words for token in tokens_filter):
                            detail[key][name_part] += prod_price

        # Sắp xếp các nhóm theo thứ tự thời gian
        if group_by == "day":
            groups = sorted(revenue.keys(), key=lambda x: datetime.strptime(x, "%d-%m-%Y"))
        elif group_by == "month":
            groups = sorted(revenue.keys(), key=lambda x: datetime.strptime("01-" + x, "%d-%m-%Y"))
        elif group_by == "year":
            groups = sorted(revenue.keys(), key=lambda x: datetime.strptime("01-01-" + x, "%d-%m-%Y"))
        else:
            groups = sorted(revenue.keys())

        fig, ax = plt.subplots(figsize=(8, 5))

        if mode == "tổng quan":
            values = [revenue[g] for g in groups]
            ax.bar(groups, values, color='skyblue')
            ax.set_ylabel("Tổng thu nhập (VNĐ)")
            ax.set_title(f"Thu nhập {group_by} (Tổng quan)")
            ax.set_xlabel("Thời gian")
        else:
            # Mode "chi tiết": vẽ grouped bar chart, mỗi sản phẩm là 1 cột riêng cho mỗi nhóm
            all_products = set()
            for g in groups:
                all_products.update(detail[g].keys())
            all_products = sorted(all_products)

            if not all_products:
                layout = self.thongkeLabel.layout()
                if layout is None:
                    layout = QVBoxLayout(self.thongkeLabel)
                    self.thongkeLabel.setLayout(layout)
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()
                from PyQt6.QtWidgets import QLabel
                msg_label = QLabel("Không có dữ liệu để hiển thị (chi tiết).")
                layout.addWidget(msg_label)
                return

            color_list = ['skyblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
            prod_colors = {}
            for i, prod in enumerate(all_products):
                prod_colors[prod] = color_list[i % len(color_list)]

            x = range(len(groups))
            bar_width = 0.8 / len(all_products)

            for i, prod in enumerate(all_products):
                prod_vals = []
                for g in groups:
                    prod_vals.append(detail[g].get(prod, 0))
                x_prod = [pos + i * bar_width for pos in x]
                ax.bar(x_prod, prod_vals, width=bar_width, color=prod_colors[prod], label=prod)
            ax.set_xticks([pos + (len(all_products) / 2 - 0.5) * bar_width for pos in x])
            ax.set_xticklabels(groups, rotation=45, ha="right")
            ax.set_ylabel("Tổng thu nhập (VNĐ)")
            ax.set_title(f"Thu nhập {group_by} (Chi tiết)")
            ax.set_xlabel("Thời gian")
            handles = [plt.Rectangle((0, 0), 1, 1, color=prod_colors[p]) for p in all_products]
            ax.legend(handles, all_products, loc='upper left', bbox_to_anchor=(1, 1))

        plt.tight_layout()

        # Đưa đồ thị vào thongkeLabel (một QLabel trong giao diện thongke.ui)
        layout = self.thongkeLabel.layout()
        if layout is None:
            layout = QVBoxLayout(self.thongkeLabel)
            self.thongkeLabel.setLayout(layout)
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()

    def Home(self):
        self.MainWindow.hide()
        from ui.Quanly.Giaodien.QuanlyExt import QuanlyExt
        self.quanly_window = QMainWindow()
        self.quanly_ui = QuanlyExt()
        self.quanly_ui.setupUi(self.quanly_window)
        self.quanly_window.show()

    def export_to_excel(self):
        """
        Xuất file Excel với cột Đồ uống (chỉ tên+size),
        mỗi ô có thể có nhiều dòng (mỗi dòng chứa tối đa 2 đồ uống).
        Cột sẽ tự động rộng vừa đủ cho dòng dài nhất trong ô.
        """
        orders = self.data_connector.get_all_orders()
        if not orders:
            QMessageBox.information(self.MainWindow, "Thông báo", "Không có đơn hàng nào để xuất.")
            return

        save_path, _ = QFileDialog.getSaveFileName(
            self.MainWindow,
            "Chọn nơi lưu file Excel",
            os.path.join(os.getcwd(), "Orders.xlsx"),
            "Excel Files (*.xlsx)"
        )
        if not save_path:
            return

        headers = ["Tên", "SĐT", "Đồ uống (tên+size)", "Tổng tiền", "Thời gian"]
        excel_data = []
        for order in orders:
            name = order.name
            sdt = getattr(order, "sdt", "")

            product_count = {}
            for prod in order.products:
                parts = prod.split(":")
                if not parts:
                    continue
                prod_text = parts[0].strip()
                product_count[prod_text] = product_count.get(prod_text, 0) + 1

            unique_products = []
            for prod_text, count in product_count.items():
                unique_products.append(f"{count} {prod_text}" if count > 1 else prod_text)

            lines = []
            for i in range(0, len(unique_products), 2):
                line = " | ".join(unique_products[i:i + 2])
                lines.append(line)
            products_str = "\n".join(lines)

            totalprice = order.totalprice
            time_str = order.time
            excel_data.append([name, sdt, products_str, totalprice, time_str])

        workbook = xlsxwriter.Workbook(save_path)
        worksheet = workbook.add_worksheet("Orders")

        default_format = workbook.add_format({'border': 1, 'text_wrap': False})
        drink_format = workbook.add_format({'border': 1, 'text_wrap': True})

        for col, header in enumerate(headers):
            worksheet.write(0, col, header, default_format)

        col_widths = [len(h) for h in headers]

        for row_idx, row_data in enumerate(excel_data, start=1):
            for col_idx, cell_value in enumerate(row_data):
                cell_str = str(cell_value)
                if col_idx == 2:
                    lines_in_cell = cell_str.split("\n")
                    max_line_length = max(len(line) for line in lines_in_cell) if lines_in_cell else 0
                    col_widths[col_idx] = max(col_widths[col_idx], max_line_length)
                    worksheet.write(row_idx, col_idx, cell_str, drink_format)
                else:
                    col_widths[col_idx] = max(col_widths[col_idx], len(cell_str))
                    worksheet.write(row_idx, col_idx, cell_str, default_format)

        for col_idx, width in enumerate(col_widths):
            worksheet.set_column(col_idx, col_idx, width + 2)

        workbook.close()
        QMessageBox.information(self.MainWindow, "Thông báo", f"Xuất file Excel thành công: {save_path}")
