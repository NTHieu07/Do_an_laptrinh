from Models.Product import Product
from libs.JsonFileFactory import JsonFileFactory

products = []
products.append(Product("Tra xanh", 700 , 10000))
products.append(Product("Nuoc ep dau",1000 ,  20000))
products.append(Product("Nuoc ep dau",700 ,  15000))
products.append(Product( "Tra C2",700 , 15000))
for product in products:
    print(product)
jff = JsonFileFactory()
filename = "../Dataset/products.json"
jff.write_data(products, filename)