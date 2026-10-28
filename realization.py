from abc import ABC, abstractmethod


class Payable(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

    @abstractmethod
    def get_receipt(self) -> str:
        pass


class Payment(Payable):
    def __init__(self, transaction_id: str):
        self.transaction_id = transaction_id
        self.is_paid = False
        self.amount = 0.0

    def pay(self, amount: float) -> bool:
        if amount > 0:
            self.amount = amount
            self.is_paid = True
            print(f"Processing payment of ${amount:.2f}...")
            return True
        return False

    def get_receipt(self) -> str:
        if self.is_paid:
            return f"Receipt [TXN #{self.transaction_id}]: Paid ${self.amount:.2f}"
        return f"Receipt [TXN #{self.transaction_id}]: Payment pending."


if __name__ == "__main__":
    payment = Payment("TX10094")
    payment.pay(149.99)
    print(payment.get_receipt())
