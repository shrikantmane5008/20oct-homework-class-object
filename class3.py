class Laptop:
    def __init__(self, brand, color, price, name, ram):
        self.brand = brand
        self.color = color
        self.price = price
        self.name = name
        self.ram = ram


laptop1 = Laptop("HP", "Silver", 45000, "Pavilion", "8GB")


laptop2 = Laptop("Dell", "Black", 55000, "Inspiron", "16GB")


laptop3 = Laptop("Lenovo", "Grey", 40000, "IdeaPad", "8GB")


laptop4 = Laptop("Asus", "Blue", 60000, "Vivobook", "16GB")


laptop5 = Laptop("Acer", "Black", 50000, "Aspire", "16GB")

laptop_list = []
laptop_list.append(laptop1)
laptop_list.append(laptop2)
laptop_list.append(laptop3)
laptop_list.append(laptop4)
laptop_list.append(laptop5)

for obj in laptop_list:
    if obj.ram =="8GB":
        print(obj.name , obj.brand)