class EncapsulatedAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Приватний баланс // Private balance

    @property
    def balance(self):
        return self.__balance   # Геттер балансу // Getter for balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value   # Сеттер балансу, перевірка на від’ємне // Setter with check for negative
        else:
            print("Баланс не може бути від’ємним")  # Повідомлення про помилку // Error message

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Додаємо до балансу // Add to balance
            print(f"Поповнено {amount}, новий баланс: {self.__balance}")
        else:
            print("Сума поповнення має бути позитивною")  # Сума поповнення позитивна // Deposit must be positive

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount # Знімаємо з балансу // Subtract from balance
            print(f"Знято {amount}, новий баланс: {self.__balance}")
        else:
            print("Недостатньо коштів або невірна сума")  # Помилка зняття // Withdrawal error


acc = EncapsulatedAccount("Anna", 1000)
acc.deposit(200)
acc.withdraw(500)
print(acc.balance)
acc.balance = -100  # Спроба встановити від’ємний баланс // Attempt to set negative balance
