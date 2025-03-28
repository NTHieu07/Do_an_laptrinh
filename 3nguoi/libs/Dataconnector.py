import os

from Models.Category import Category
from Models.Employee import Employee
from Models.Order import Order
from Models.Product import Product
from libs.JsonFileFactory import JsonFileFactory


class DataConnector:
    def __init__(self):
        self.json_factory = JsonFileFactory()
        # Đường dẫn đến file JSON (dùng raw string cho Windows)
        self.products_file = r"../Dataset/products.json"
        self.categories_file = r"../Dataset/categories.json"
        self.order_file = r"../Dataset/order.json"
    def get_all_products(self):
        products = []
        jff = JsonFileFactory()
        filename = self.products_file
        products = jff.read_data(filename , Product)
        return products
    def get_all_categories(self):
        categories = []
        jff = JsonFileFactory()
        filename = self.categories_file
        Categories = jff.read_data(filename , Category)
        return Categories
    def get_all_orders(self):
        orders = []
        jff = JsonFileFactory()
        filename = self.order_file
        orders = jff.read_data(filename , Order)
        return orders
    def save_all_products(self, product_list):
        """
        Lưu danh sách sản phẩm (danh sách các đối tượng Product hoặc dictionary)
        vào file JSON.
        """
        folder = os.path.dirname(self.products_file)
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.json_factory.write_data(product_list, self.products_file)

    def save_all_categories(self, category_list):
        """
        Lưu danh sách danh mục (danh sách các đối tượng Category hoặc dictionary)
        vào file JSON.
        """
        folder = os.path.dirname(self.categories_file)
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.json_factory.write_data(category_list, self.categories_file)
    def get_all_employees(self):
        employees = []
        jff = JsonFileFactory()
        filename = r"../Dataset/database.json"
        employees = jff.read_data(filename , Employee)
        return employees