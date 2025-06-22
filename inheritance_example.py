# Базовий клас Animal // Base class Animal
class Animal:
    def __init__(self, name):
        self.name = name                            # Ім'я тварини // Animal's name

    def speak(self):
        print(f"{self.name} видає звук")           # Загальний звук тварини // Generic animal sound

    def move(self):
        print(f"{self.name} рухається")            # Загальний рух тварини // Generic movement


# Наслідування від Animal // Inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)                     # Виклик конструктора батьківського класу // Call parent constructor
        self.breed = breed                         # Порода собаки // Dog breed

    # Перевизначення методу speak // Override speak method
    def speak(self):
        print(f"{self.name} гавкає: Гав-гав!")    # Собака гавкає // Dog barks

    def fetch(self, item):
        print(f"{self.name} приносить {item}")    # Метод fetch, який є у Dog // Dog fetches an item


# Наслідування від Animal // Inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)                     # Виклик конструктора батьківського класу // Call parent constructor
        self.color = color                         # Колір кота // Cat color

    # Перевизначення методу speak // Override speak method
    def speak(self):
        print(f"{self.name} нявкає: Мяу!")        # Кіт нявкає // Cat meows

    def scratch(self):
        print(f"{self.name} дряпає меблі")        # Метод scratch для кота // Cat scratches furniture



dog = Dog("Шарік", "Овчарка")
cat = Cat("Мурка", "Сірий")

dog.speak()         # Шарік гавкає: Гав-гав!
dog.move()          # Шарік рухається
dog.fetch("м'яч")   # Шарік приносить м'яч

cat.speak()         # Мурка нявкає: Мяу!
cat.move()          # Мурка рухається
cat.scratch()       # Мурка дряпає меблі


# Перевірка типу об'єкту за допомогою isinstance // Type checking with isinstance
print(isinstance(dog, Animal))     # True, бо Dog наслідується від Animal
print(isinstance(cat, Dog))        # False, Cat не є Dog

# Перевірка класу об'єкту // Checking object's class
print(type(dog))                   # <class '__main__.Dog'>
print(type(cat))                   # <class '__main__.Cat'>
