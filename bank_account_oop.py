# Міні-проєкт банківського акаунта з використанням ООП
# Bank account mini-project using OOP principles

# Базовий клас акаунта
# Base Account class
class Account:
    def __init__(self, owner, balance):
        self.owner = owner                # Ім'я власника акаунта // Account owner's name
        self._balance = balance           # Захищений атрибут балансу // Protected balance attribute

    def deposit(self, amount):
        # Додає кошти на рахунок // Adds money to the account
        if amount > 0:
            self._balance += amount
            print(f"{amount} грн зараховано. Баланс: {self._balance} грн")  # Deposited
        else:
            print("Сума має бути більшою за 0")  # Amount must be greater than 0

    def withdraw(self, amount):
        # Знімає кошти з рахунку // Withdraws money from the account
        if amount <= self._balance:
            self._balance -= amount
            print(f"{amount} грн знято. Баланс: {self._balance} грн")  # Withdrawn
        else:
            print("Недостатньо коштів!")  # Insufficient funds

    def get_balance(self):
        # Повертає поточний баланс // Returns current balance
        return self._balance


# Дочірній клас — ощадний рахунок
# Child class — Savings Account
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # Відсоткова ставка // Interest rate

    def apply_interest(self):
        # Нараховує відсотки на залишок // Applies interest to the balance
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Нараховано {interest:.2f} грн відсотків. Баланс: {self._balance:.2f} грн")


# Дочірній клас — поточний рахунок
# Child class — Checking Account
class CheckingAccount(Account):
    def __init__(self, owner, balance, transaction_fee):
        super().__init__(owner, balance)
        self.transaction_fee = transaction_fee  # Комісія за транзакцію // Transaction fee

    def withdraw(self, amount):
        # Знімає кошти з урахуванням комісії // Withdraws money with fee
        total = amount + self.transaction_fee
        if total <= self._balance:
            self._balance -= total
            print(f"{amount} грн знято + {self.transaction_fee} грн комісія. Баланс: {self._balance} грн")
        else:
            print("Недостатньо коштів з урахуванням комісії!")  # Insufficient with fee


# Демонстрація
# Demonstration
print("=== Savings Account ===")
savings = SavingsAccount("Анна", 1000, 0.05)
savings.deposit(500)
savings.withdraw(300)
savings.apply_interest()

print("\n=== Checking Account ===")
checking = CheckingAccount("Богдан", 800, 10)
checking.deposit(200)
checking.withdraw(500)
checking.withdraw(600)  # Недостатньо коштів
