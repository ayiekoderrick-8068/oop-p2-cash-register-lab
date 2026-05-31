#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize properties; assigning to self.discount triggers the setter validation
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Task 3 Step 3: Ensure discount is an integer between 0-100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        # Task 3 Step 4: Add price to total and update items list
        self.total += price * quantity
        
        for _ in range(quantity):
            self.items.append(item)
        
        # Track transaction for voiding capabilities
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # Task 3 Step 4: Check if there are transactions or a valid discount
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        # Apply the discount percentage
        self.total -= self.total * (self.discount / 100)
        
        # Match the exact string format expected by TestCashRegister ($800 with no decimals)
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        # Task 3 Step 4: Error handling for empty transactions
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Revert the total and remove the last record
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        
        # Prevent negative totals
        if self.total < 0:
            self.total = 0.0

        # Remove the items from the items list
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
