class Category:
    def __init__(self, name , products):
        self.name = name
        self.products = products
    def __str__(self):
        print(self.name)
        for i in range(0 , len(self.products)):
            p = self.products[i]
            product = p + "\n"
            print(product)
        return ""
