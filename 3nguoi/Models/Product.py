class Product:
    def __init__(self , name, size ,price , danh_muc = None , image_path = None):
        self.name = name
        self.size = size
        self.price = price
        self.danh_muc = danh_muc
        self.image_path = image_path
    def __str__(self):
        return f'{self.name} {self.size}ml : {self.price} (Image: {self.image_path})'