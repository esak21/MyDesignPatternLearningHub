from PaymentStrategy import PaymentStrategy
class PaymentProcessor:

    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount: int ):
        self.strategy.pay(amount)
