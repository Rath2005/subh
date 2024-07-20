#Program to create an abstract class paymentMethod with an abstract method pay

from abc import ABC, abstractmethod

# Abstract class PaymentMethod

class PaymentMethod(ABC):

    @abstractmethod

    def pay(self):

        pass

# CreditCard subclass

class CreditCard(PaymentMethod):

    def _init_(self, cc_no, exp_date, cvv):

        self.cc_no = cc_no

        self.exp_date = exp_date

        self.cvv = cvv
    
    def pay(self):

        # Simulate a credit card payment

        return f"Processing credit card payment with card number {self.cc_no}"

# PayPal subclass

class PayPal(PaymentMethod):

    def _init_(self, email):

        self.email = email
    
    def pay(self):

        # Simulate a PayPal payment

        return f"Processing PayPal payment for email {self.email}"

# Bitcoin subclass

class Bitcoin(PaymentMethod):

    def _init_(self, wallet_add):

        self.wallet_add = wallet_add
    
    def pay(self):

        # Simulate a Bitcoin payment

        return f"Processing Bitcoin payment to wallet address {self.wallet_add}"

# Example Usage

if __name__ == "_main_":

    # Creating instances

    credit_card = CreditCard(cc_no="1234-5678-9876-5432", exp_date="12/25", cvv="123")

    paypal = PayPal(email="user@example.com")

    bitcoin = Bitcoin(wallet_add="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    
    # Processing payments

    print(credit_card.pay())

    print(paypal.pay())
    
    print(bitcoin.pay())