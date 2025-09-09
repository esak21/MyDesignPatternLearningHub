from Processor import PaymentProcessor
from cryptoPayment import cryptoPayment


processor = PaymentProcessor(cryptoPayment())
processor.process_payment(250)