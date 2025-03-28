from Models.Category import Category
from libs.JsonFileFactory import JsonFileFactory

jff = JsonFileFactory()
filename = "../Dataset/categories.json"
cate = jff.read_data(filename , Category)
for c in cate:
    print(c)