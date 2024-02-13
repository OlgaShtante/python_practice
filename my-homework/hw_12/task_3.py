class Vehicle:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self) -> None:
        print("The vehicle is starting")

class Car(Vehicle):
    def __init__(self, brand: str, model: str, color: str, doors: int):
        super().__init__(brand, model, color)
        self.doors = doors
        print(f"\n{color} {brand} {model} with {doors} doors")

    def honk(self) -> None:
        print("The car is honking")

class Bike(Vehicle):
    def __init__(self, brand: str, model: str, color: str, gears: int):
        super().__init__(brand, model, color)
        self.gears = gears
        print(f"\n{color} {brand} {model} with {gears} gears")

    def pedal(self) -> None:
        print("The bike is pedaling")

class Plane(Vehicle):
    def __init__(self, brand: str, model: str, color: str, wingspan: float):
        super().__init__(brand, model, color)
        self.wingspan = wingspan
        print(f"\n{color} {brand} {model} with {wingspan} wingspan")

    def fly(self) -> None:
        print("The plane is flying")


if __name__ == "__main__":
    car = Car("Tesla", "X", "White", 5)
    car.start()
    car.honk()

    bike = Bike("Scott", "Mountain Bike", "Black", 22)
    bike.start()
    bike.pedal()

    plane = Plane("Boeing", "777", "Grey", 64.8)
    plane.start()
    plane.fly()
