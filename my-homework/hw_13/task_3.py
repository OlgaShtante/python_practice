class Animal:
    def __init__(self, name: str, wingspan: float):
        self.name = name
        self.wingspan = wingspan

class FlyingAnimal(Animal):
    def fly(self) -> None:
        print('Animal can fly.')

class Bird(FlyingAnimal):
    def fly(self) -> None:
        print(f"{self.name} is flying with wingspan {self.wingspan}.")

class Bat(FlyingAnimal):
    def fly(self) -> None:
        print(f"{self.name} is flying with wingspan {self.wingspan} using echolocation.")

class Penguin(Animal):
    def __init__(self, name: str, wingspan: float):
        super().__init__(name, wingspan)



if __name__ == "__main__":
    bird = Bird("Sparrow", 0.3)
    bird.fly()

    bat = Bat("Bat", 0.4)
    bat.fly()

    penguin = Penguin("Pinguin", 0.5)
    try:
        penguin.fly()
    except AttributeError as error_msg:
        print(f'Pinguin cannot fly! Error: {error_msg}.')