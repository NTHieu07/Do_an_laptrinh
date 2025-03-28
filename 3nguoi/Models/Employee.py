class Employee:
    def __init__(self,ten,id,gioi_tinh, ngay_sinh, chuc_vu):
        self.ten=ten
        self.id=id
        self.gioi_tinh=gioi_tinh
        self.ngay_sinh=ngay_sinh
        self.chuc_vu=chuc_vu
    def __str__(self):
        if self.gioi_tinh==True:
            return self.ten +" - " + self.id + " - " + self.ngay_sinh+" - " + self.chuc_vu
        else:
            return self.ten + " - " + self.id  + " - " + self.ngay_sinh+" - " + self.chuc_vu