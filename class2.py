class Car:
    def __init__(self, brand, color, price, model, model_type):
        self.brand = brand
        self.color = color
        self.price = price
        self.model = model
        self.model_type = model_type


car1 = Car("BMW", "Black", 15000000, "M4", "Coupe")

car2 = Car("Dodge", "Red", 8000000, "Dodge Challenger", "Muscle Car")

car3 = Car("Land Rover", "White", 10000000, "Defender", "SUV")

car4 = Car("Toyota", "Black", 4000000, "Fortuner", "SUV")

car5 = Car("Tata", "Silver", 1500000, "Sierra", "SUV")

car_list =[]
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)
car_list.append(car4)
car_list.append(car5)

for obj in car_list:
    # if obj.price > 1000000:
    #     print(obj.brand,obj.model,obj.model_type)

    print(f"Brand: {obj.brand}, Color: {obj.color}, Price: ₹{obj.price}, Model: {obj.model}, Type: {obj.model_type}")