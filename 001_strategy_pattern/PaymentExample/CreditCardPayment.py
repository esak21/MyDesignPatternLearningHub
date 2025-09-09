from PaymentStrategy import PaymentStrategy

class CreditCardpayment(PaymentStrategy):

    def pay(self, card):
        print("we are paying the fee using the credit card ")