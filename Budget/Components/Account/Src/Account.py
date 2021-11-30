from .TransactionData import TransactionData


class Account:
    def __init__(self):
        self._balance: float = 0
        self._history: list = []

    def deposit(self, amount: float, description: str, tags: list = []) -> None:
        # Should date argument be added to deposit?
        pass

    def withdraw(self, amount: float, description: str, tags: list = []) -> None:
        pass

    def balance(self) -> float:
        return self._balance

    def get_history(self) -> list:
        return self._history