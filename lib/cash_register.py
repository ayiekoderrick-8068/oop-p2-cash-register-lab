#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize properties using the setter logic for validation
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer between 0-100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            # Default to 0 if invalid as per instructions
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        # Add price to total and update item tracking
        self.total += price * quantity
        
        # Add item name to the list for each unit purchased
        for _ in range(quantity):
            self.items.append(item)
        
        # Record transaction details for voiding capabilities
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Apply discount percentage to the total
        self.total -= self.total * (self.discount / 100)
        
        # Formatting total to match the specific string format expected by the tests
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Remove the last transaction record and update the total
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        
        if self.total < 0:
            self.total = 0.0

        # Remove the specific units from the items list
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
