from validate_sku_number import validate_sku_number
from tpl_to_dct import tpl_to_dct


def reconcile_inventory(physical_counts, ledger):

    inventory_reconciliation = {}

    lookup_dictionary = {}
    for ldgr in ledger:
        sku_number, count = ldgr
        if validate_sku_number(sku_number):
            lookup_dictionary.update(
                tpl_to_dct(ldgr)
            )

    for count in physical_counts:
        sku_number = count.get("sku")
        if validate_sku_number(sku_number):
            if sku_number in lookup_dictionary:
                difference = count.get("physical_count") - lookup_dictionary[sku_number].get("ledger_count")
                if difference != 0:
                    inventory_reconciliation.update(
                        {
                            sku_number: dict(
                                name = count.get("name"),
                                difference = difference
                            )
                        }
                    )
            else:
                inventory_reconciliation.update(
                    {
                        sku_number: dict(
                        name = "Unknown Product",
                        difference = "MISSING_FROM_LEDGER"
                        )
                    }
                )
    
    for ldgr in lookup_dictionary:
        if ldgr not in inventory_reconciliation:
            inventory_reconciliation.update(
                    {
                        ldgr: dict(
                        name = "Unknown Product",
                        difference = "MISSING_FROM_PHYSICAL"
                        )
                    }
                )
    
    return inventory_reconciliation


if __name__ == "__main__":
    # System A: Physical Warehouse Counts (List of Dictionaries)
    physical_inventory = [
        {"sku": "SKU-101", "name": "Wireless Mouse", "physical_count": 45},
        {"sku": "SKU-102", "name": "Mechanical Keyboard", "physical_count": 12},
        {"sku": "SKU-103", "name": "USB-C Cable", "physical_count": 110},
        {"sku": "SKU-104", "name": "HDMI Switch", "physical_count": 25},
        {"sku": "CORRUPT_DATA", "name": "Unknown Item", "physical_count": 0}, # Invalid SKU format!
        {"sku": "SKU-105", "name": "Noise Cancelling Headphones", "physical_count": 8} # Missing from Digital Ledger!
    ]

    # System B: Digital Ledger Balances (List of Tuples)
    # Format: (sku_string, expected_ledger_count)
    digital_ledger = [
        ("SKU-101", 45),   # Perfect Match
        ("SKU-102", 15),   # Mismatch! (12 vs 15)
        ("SKU-103", 100),  # Mismatch! (110 vs 100)
        ("SKU-104", 25),   # Perfect Match
        ("SKU-106", 50)    # Missing from Physical Inventory!
    ]

    print(reconcile_inventory(
        physical_inventory, digital_ledger
    ))