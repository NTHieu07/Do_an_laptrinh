from Models.Category import Category
from Models.Product import Product
from libs.JsonFileFactory import JsonFileFactory
jff = JsonFileFactory()
fileproduct = "../Dataset/products.json"
filecate = "../Dataset/categories.json"

categories = []
cate1 = Category("Trà" , [])
cate2 = Category("Nước ép", [])
cate3 = Category("Cà phê", [])
cate4 = Category("Sinh tố" , [])
products = jff.read_data(fileproduct , Product)
for product in products:
    if "trà" in product.name.lower():
        cate1.products.append(product)
    elif "ép" in product.name.lower():
        cate2.products.append(product)
    elif "cà phê" in product.name.lower():
        cate3.products.append(product)
    elif "sinh tố" in product.name.lower():
        cate4.products.append(product)
categories.append(cate1)
categories.append(cate2)
categories.append(cate3)
categories.append(cate4)
jff.write_data(categories, filecate)

