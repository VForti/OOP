# Поліморфізм у дії // Polymorphism in action

class Shape:
    def area(self):
        # Метод, який повинен бути перевизначений у підкласах
        # Method meant to be overridden in subclasses
        raise NotImplementedError("Цей метод має бути реалізований у підкласі") 

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        # Обчислення площі прямокутника
        # Calculate rectangle area
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # Обчислення площі кола
        # Calculate circle area
        import math
        return math.pi * (self.radius ** 2)

def print_area(shape):
    # Функція приймає будь-який об'єкт з методом area()
    # Function accepts any object with an area() method
    print(f"Площа фігури: {shape.area():.2f}")

# Створення об'єктів різних класів
# Creating instances of different classes
rect = Rectangle(5, 10)
circle = Circle(7)

print_area(rect)      # Площа фігури: 50.00
print_area(circle)    # Площа фігури: 153.94
