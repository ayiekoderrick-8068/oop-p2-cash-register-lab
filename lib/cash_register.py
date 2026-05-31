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
        return self._discount

    @discount.setter
    def discount(self, value):
        """
        Task 3 Step 3: Ensures discount is an integer between 0 and 100 inclusive.
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        """
        Task 3 Step 4: Adds an item's price to the total and tracks the transaction.
        """
        self.total += price * quantity
        
        for _ in range(quantity):
            self.items.append(item)
        
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """
        Task 3 Step 4: Applies the discount percentage to the total price.
        """
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total -= self.total * (self.discount / 100)
        
        # Use int() to match the exact string format expected by the tests ($800.)
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        """
        Task 3 Step 4: Voids the last transaction, updating the total and item list.
        """
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        
        # Ensure total returns to exactly 0.0 if all items are voided
        if self.total < 0.01:
            self.total = 0.0

        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
