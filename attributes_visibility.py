"""
Demonstration of public, protected, and private attributes.
Демонстрація публічних, захищених і приватних атрибутів у Python.
"""

class DemoAccess:
    def __init__(self):
        self.public_attr = "I am public"             # Public attribute — accessible anywhere // Публічний атрибут — доступний звідусіль
        self._protected_attr = "I am protected"       # Protected attribute — by convention, used within class or subclass // Захищений атрибут — за домовленістю, використовується в класі чи підкласі
        self.__private_attr = "I am private"          # Private attribute — name mangled, can't access directly from outside // Приватний атрибут — не доступний напряму зовні

    def show_attributes(self):
        # Method to print all attributes from inside the class // Метод для виводу всіх атрибутів зсередини класу
        print("Inside class:")
        print("Public:", self.public_attr)
        print("Protected:", self._protected_attr)
        print("Private:", self.__private_attr)


# Creating an instance of DemoAccess // Створення екземпляру класу
obj = DemoAccess()

# Accessing attributes from outside the class // Доступ до атрибутів ззовні класу
print("Outside class:")
print("Public:", obj.public_attr)  # ✅ Allowed // Дозволено

print("Protected:", obj._protected_attr)  # ⚠️ Possible, but not recommended // Можна, але не рекомендується

# print("Private:", obj.__private_attr)  # ❌ Will raise AttributeError // Спроба — помилка (недоступний)

# Accessing private attribute using name mangling // Доступ до приватного атрибута
print("Private: ", obj._DemoAccess__private_attr)

# Call internal method to show all attributes // Виклик методу класу для демонстрації атрибутів
obj.show_attributes()
