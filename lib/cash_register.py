#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Task 3 Step 2: Initialize attributes
        # Assigning to self.discount triggers the @setter validation
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Returns the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        # Task 3 Step 3: Ensure discount is an integer between 0-100 inclusive.
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        """Increases total, updates items list, and records the transaction."""
        self.total += price * quantity
        
        # Add individual item names to the items list (supports multiples)
        for _ in range(quantity):
            self.items.append(item)
        
        # Store transaction details for future voiding or discounting logic
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Reduces total by the discount percentage if transactions exist."""
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        # Apply the percentage discount
        self.total -= self.total * (self.discount / 100)
        
        # Formatting: Match the exact success message expected by tests ($800.)
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """Removes the most recent transaction and adjusts total and items."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Pop the last transaction from the history
        last = self.previous_transactions.pop()
        
        # Deduct the exact amount for that transaction
        self.total -= last["price"] * last["quantity"]
        
        # Handle potential floating point issues to ensure it returns to exactly 0.0
        if self.total < 0.001:
            self.total = 0.0

        # Remove the specific items added in that transaction from the inventory list
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
