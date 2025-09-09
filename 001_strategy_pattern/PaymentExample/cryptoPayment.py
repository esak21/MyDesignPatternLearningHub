from PaymentStrategy import PaymentStrategy

class cryptoPayment(PaymentStrategy):

    def pay(self, card):
        print("we are paying the fee using the Crypto Method ")