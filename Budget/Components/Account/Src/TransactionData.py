import datetime as dt

from Budget.Utils import generate_unique_id


class TransactionData:
    def __init__(self, amount: float, date: dt.date, description: str, tags: list):
        self._amount: float = amount
        self._date: dt.date = date
        self._description: str = description
        self._tags: list = tags

        self._id: str = generate_unique_id()

    def get_amount(self) -> float:
        return self._amount

    def get_date(self) -> dt.date:
        return self._date

    def get_description(self) -> str:
        return self._description

    def get_tags(self) -> list:
        return self._tags

    def get_id(self) -> str:
        return self._amount

    def set_amount(self, amount: float) -> None:
        self._amount = amount

    def set_date(self, date: dt.date) -> None:
        self._date = date

    def set_description(self, description: str) -> None:
        self._description = description

    def clear_tags(self) -> None:
        self._tags = []

    def remove_tag(self, tag: str) -> None:
        try:
            self._tags.remove(tag)
        except ValueError:
            print(f"Object has no tag \"{tag}\"")

    def add_tag(self, tag: str) -> None:
        if tag in self._tags:
            print(f"Tag \"{tag}\" already exist")
        else:
            self._tags.append(tag)
