class ShoppingCart:

    STORE_INVENTORY = {"laptop", "mouse", "keyboard", "monitor"}

    def __init__(self, customer_name):

        self.customer_name = customer_name
        self.items = []

    
    def add_item(self, item_name, quantity, price_per_unit):

        if item_name in self.STORE_INVENTORY:
            self.items.append((item_name, quantity, price_per_unit))

        else:
            print(f"We do not sell {item_name}!")


    def get_total_bill(self):

        total = 0

        for item in self.items:
            name, quantity, price_per_unit = item
            total += (quantity * price_per_unit)

        return total



if __name__ == "__main__":
     # 1. Instantiate a fresh cart object for a customer
    alice_cart = ShoppingCart("Alice")

    # 2. Add valid items
    alice_cart.add_item("laptop", quantity=1, price_per_unit=899.99)
    alice_cart.add_item("mouse", quantity=2, price_per_unit=25.50)

    # 3. Attempt to add an invalid item (Should print a warning and skip)
    alice_cart.add_item("coffee_maker", quantity=1, price_per_unit=45.00)

    # 4. Check the bill
    print(f"Customer: {alice_cart.customer_name}")
    print(f"Total Bill USD: {alice_cart.get_total_bill()}")