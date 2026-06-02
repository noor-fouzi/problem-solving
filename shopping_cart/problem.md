## 🚀 Problem 11: The E-Commerce Smart Shopping Cart
**Level:** Medium-Hard (Week 3 Control Flow + Intro to OOP)

**Scenario:** Instead of using raw dictionaries to track customer items, we are going to build an interactive, smart object-oriented shopping cart system that calculates totals, manages quantities, and enforces item whitelists.

## 📋 System Requirements
Write a Python class named `ShoppingCart`. Every individual cart object must track the customer's name and a list of items inside it.

## Your Structural Constraints:
1. **The Constructor** (`__init__`): The class must accept a string `customer_name` when created. It must also automatically initialize an empty list attribute called `items` to hold the inventory.

2. **The Whitelist Set:** Inside the class, create or reference a class-level whitelist set of accepted store items:
`STORE_INVENTORY = {"laptop", "mouse", "keyboard", "monitor"}`

3. **Method 1:** `add_item(self, item_name, quantity, price_per_unit)`

    - **Control Flow Guardrail:** If the `item_name` is **not** in `STORE_INVENTORY`, print a warning message: `"Warning: We do not sell [item_name]!"` and do not add it to the cart.

    - If it *is* valid, append a tuple or small dictionary representing `(item_name, quantity, price_per_unit)` into the cart's internal `items` list.

4. **Method 2:** `get_total_bill(self)`

    - This method must loop through all items currently in the cart's internal list, calculate the total cost, and return the final dollar amount as a **pure float rounded to 2 decimal places**.

## 🎯 Expected Execution Layout
Your script should be able to run this exact test code inside its `if __name__ == "__main__":` block:

```Python
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
```
## Expected Console Output:

```Plaintext
Warning: We do not sell coffee_maker!
Customer: Alice
Total Bill USD: 950.99
```