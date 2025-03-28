from datetime import datetime

class Order:
    def __init__(self, name = None, sdt = None ,products = None , totalprice = None, time=None):
        self.name = name
        self.sdt = sdt
        self.products = products
        self.totalprice = totalprice
        self.time = time if time else datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Lưu thời gian khi đơn hàng được tạo
    def __str__(self):
        print(f"tên khách hàng: {self.name}")
        print(f"số điện thoại: {self.sdt}")
        print("Danh sách mua hàng: ")
        for product in self.products:
            print(f"\t{product}")
        print(f"tổng giá tiền: {self.totalprice} VNĐ")
        print(f"thời gian mua: {self.time}")
        return ""