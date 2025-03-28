from datetime import datetime

from Models.Category import Category
from Models.Order import Order
from Models.Product import Product
from libs.JsonFileFactory import JsonFileFactory

ketqua = []
n = 0
jff = JsonFileFactory()
filecate = "../Dataset/categories.json"
fileproduct = "../Dataset/products.json"
fileorder = "../Dataset/order.json"
filethanhtien = "../Dataset/thanhtien.json"
products = jff.read_data(fileproduct , Product)
cate = jff.read_data(filecate , Category)
for c in cate:
    print(c)

def mua_do_uong(n):
    print("#" * 30)
    giatien = 0
    order = []
    donhang = input("ban muon chon loai nuoc uong nao : ")
    mua = Order(f"khach hang {n}" , time = datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    for i in range(0 , len(products)):
        if products[i].name.lower() in donhang.lower():
            order.append(products[i])
            giatien = products[i].price + giatien
    print(f"vay ban da chon {len(order)} do uong va tong gia tien la {giatien} dong")
    mua.totalprice = giatien
    mua.products = order
    ketqua.append(mua)
    jff.write_data(ketqua , fileorder)

while True:
    n += 1
    traloi = input("ban co muon mua do uong?: ")
    if traloi.lower == "yes" or traloi.lower() == "co":
        mua_do_uong(n)
    else:
        break