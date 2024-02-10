from typing import List

class BankAccount:
    def __init__(self, number: str, owner: str, balance: float):
        self.number = number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def transfer(self, recipient: 'BankAccount', amount: float) -> None:
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            recipient.deposit(amount)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.accounts: List[BankAccount] = []

    def get_total_balance(self) -> float:
        total_balance = sum(account.balance for account in self.accounts)
        return total_balance


if __name__ == "__main__":
    account = BankAccount("12345", "Test Account", 1000.0)
    person = Person("Test Account", 21)
    person.accounts.append(account)

    account.deposit(1500.0)
    account.withdraw(900.0)

    new_account = BankAccount("67890", "New Test Account", 800.0)
    account.transfer(new_account, 300.0)

    total_balance = person.get_total_balance()
    print(f"Total balance for {person.name}: {total_balance}") #1300
