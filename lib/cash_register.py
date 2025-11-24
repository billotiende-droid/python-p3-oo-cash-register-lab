#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self.total += amount
        self.items.extend([title] * quantity)
        self.last_transaction = {'amount': amount, 'count': quantity}

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

   