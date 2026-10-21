class Mobile:
    def __init__(self, brand, color, price, name, storage):
        self.brand = brand
        self.color = color
        self.price = price
        self.name = name
        self.storage = storage


mobile1 = Mobile("Samsung", "Black", 20000, "Galaxy M35", "128GB")


mobile2 = Mobile("Apple", "White", 70000, "iPhone 15", "256GB")


mobile3 = Mobile("Vivo", "Blue", 18000, "Vivo T3", "128GB")


mobile4 = Mobile("Oppo", "Green", 22000, "Oppo F27", "256GB")


mobile5 = Mobile("OnePlus", "Black", 35000, "Nord 4", "512GB")

Mobile_list =[]
Mobile_list.append(mobile1)
Mobile_list.append(mobile2)
Mobile_list.append(mobile3)
Mobile_list.append(mobile4)
Mobile_list.append(mobile5)

for obj in Mobile_list:
    print(f"mobile name is --{obj.name} ,and mobile color is a {obj.color}")