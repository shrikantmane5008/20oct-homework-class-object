class Watch:
    def __init__(self, brand, color, price, name, type):
        self.brand = brand
        self.color = color
        self.price = price
        self.name = name
        self.type = type


watch1 = Watch("Titan", "Black", 3000, "Neo", "Analog")


watch2 = Watch("Casio", "Silver", 5000, "G-Shock", "Digital")


watch3 = Watch("Apple", "Black", 30000, "Watch SE", "Smartwatch")


watch4 = Watch("Fastrack", "Blue", 2500, "Reflex", "Analog")


watch5 = Watch("Samsung", "Grey", 20000, "Galaxy Watch", "Smartwatch")

watch_list = []
watch_list.append(watch1)
watch_list.append(watch2)
watch_list.append(watch3)
watch_list.append(watch4)
watch_list.append(watch5)

for obj in watch_list :
    print (obj.brand , obj.type)