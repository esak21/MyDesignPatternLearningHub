from PaymentStrategy import PaymentStrategy

class PayPaldpayment(PaymentStrategy):

    def pay(self, card):
        print("we are paying the fee using the Pay Pal Online Method ")