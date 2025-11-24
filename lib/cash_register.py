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

   