import datetime as dt


from .TransactionData import TransactionData


class Account:
    def __init__(self):
        self._balance: float = 0.0
        self._history: list = []

    def deposit(self, amount: float, date: dt.date, description: str, tags: list = []) -> None:
        if type(amount) is not float:
            amount = float(amount)
        tags.append("deposit")
        data: TransactionData = TransactionData(amount, date, description, tags)

        self._balance += amount
        self._history.append(data)

    def withdraw(self, amount: float, date: dt.date, description: str, tags: list = []) -> None:
        if type(amount) is not float:
            amount = float(amount)
        tags.append("withdraw")
        data: TransactionData = TransactionData(amount, date, description, tags)

        self._balance -= amount
        self._history.append(data)

    def balance(self) -> float:
        return self._balance

    def get_history(self) -> list:
        return self._history
