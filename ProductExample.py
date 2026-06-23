class Product:

    #constructor
    def __init__(self,name,price,qty):
        self.name=name
        self.price=price
        self.qty=qty

    def StoreData(self):
        print(f"Name: {self.name} Price: {self.price} Quantity: {self.qty}")

p=Product('Washing Machine',30000,2)
p2=Product('Iron',5000,4)
p3=Product('Tv',50000,1)
p4=Product('Refrigerator',25000,3)

p.StoreData()
        