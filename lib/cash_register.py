#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes the CashRegister with an optional discount percentage.
        """
        # Assigning to self.discount triggers the @setter validation logic
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Gets the current discount percentage."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """
        Step 3: Ensures discount is an integer between 0 and 100 inclusive.
        Prints an error and defaults to 0 if the input is invalid.
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0  # Default to 0 if invalid as per instructions

    def add_item(self, item, price, quantity=1):
        """
        Step 4: Adds an item's price to the total and tracks the transaction.
        Updates the total, the list of items, and the transaction history.
        """
        self.total += price * quantity
        
        # Add individual item names to the items list for quantity tracking
        for _ in range(quantity):
            self.items.append(item)
        
        # Record transaction details to allow for voiding later
        self.previous_transactions.append({
            "item": item, "price": price, "quantity": quantity
        })

    def apply_discount(self):
        """
        Step 4: Applies the discount percentage to the current total.
        Validates that transactions exist and a discount is set before applying.
        """
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total -= self.total * (self.discount / 100)
        
        # Matches test_apply_discount_success_message expectation (e.g., "$800.")
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """
        Step 4: Voids the most recent transaction.
        Subtracts price and quantity from total and removes items from the list.
        """
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        
        # Handle floating point precision to ensure total returns to 0.0
        if self.total < 1e-9:
            self.total = 0.0

        # Remove specific item instances from the list
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
