class BMW:
    def fuel_type(self):
        print("BMW uses Diesel.")

    def max_speed(self):
        print("BMW max speed is 250 km/h.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol.")

    def max_speed(self):
        print("Ferrari max speed is 350 km/h.")

car1 = BMW()
car2 = Ferrari()

for car in (car1, car2):
    car.fuel_type()
    car.max_speed()