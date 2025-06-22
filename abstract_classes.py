from abc import ABC, abstractmethod

# Абстрактний клас Vehicle // Abstract class Vehicle
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start_engine(self):
        # Абстрактний метод, який має бути реалізований у підкласах
        # Abstract method to be implemented by subclasses
        pass

    @abstractmethod
    def stop_engine(self):
        # Ще один абстрактний метод
        # Another abstract method
        pass

# Конкретний клас Car наслідує Vehicle // Concrete class Car inherits Vehicle
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.brand} engine started")

    def stop_engine(self):
        print(f"{self.brand} engine stopped")

# Конкретний клас Motorcycle наслідує Vehicle // Concrete class Motorcycle inherits Vehicle
class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.brand} motorcycle engine started")

    def stop_engine(self):
        print(f"{self.brand} motorcycle engine stopped")


# Спроба створити об'єкт Vehicle викличе помилку
# Creating Vehicle instance raises error
# vehicle = Vehicle("Generic")  # TypeError: Can't instantiate abstract class

# Створюємо об'єкти конкретних класів
car = Car("Toyota")
motorcycle = Motorcycle("Harley-Davidson")

car.start_engine()        # Toyota engine started
car.stop_engine()         # Toyota engine stopped

motorcycle.start_engine() # Harley-Davidson motorcycle engine started
motorcycle.stop_engine()  # Harley-Davidson motorcycle engine stopped
