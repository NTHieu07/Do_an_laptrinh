from Models.Product import Product
from libs.JsonFileFactory import JsonFileFactory

jff = JsonFileFactory()
filename = "../Dataset/products.json"
products = jff.read_data(filename , Product)
for product in products:
    print(product)