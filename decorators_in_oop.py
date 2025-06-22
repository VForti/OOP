# Демонстрація використання декораторів в ООП
# Demonstration of decorators usage in OOP

def debug_method(func):
    # Декоратор для логування виклику методу
    # Decorator for logging method calls
    def wrapper(self, *args, **kwargs):
        print(f"Виклик методу {func.__name__} з аргументами {args} {kwargs}")
        result = func(self, *args, **kwargs)
        print(f"Метод {func.__name__} повернув {result}")
        return result
    return wrapper

class Calculator:
    def __init__(self):
        self.value = 0

    @debug_method
    def add(self, amount):
        # Додає amount до self.value
        # Adds amount to self.value
        self.value += amount
        return self.value

    @debug_method
    def multiply(self, factor):
        # Множить self.value на factor
        # Multiplies self.value by factor
        self.value *= factor
        return self.value

calc = Calculator()
calc.add(10)        # Логи виклику і результату
calc.multiply(5)    # Логи виклику і результату
