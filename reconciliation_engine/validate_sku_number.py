import re


def validate_sku_number(sku_number):
    if re.match(r"^SKU-[0-9]+$", sku_number):
        return True
    else:
        return False


if __name__ == "__main__":

    digital_ledger = [
        ("SKU-101", 45),
        ("SKU-102", 15),
        ("SKU-103", 100),
        ("SKU-104", 25),
        ("SKU-106", 50),
        ("CORRUPTED", 0)
    ]

    for ledger in digital_ledger:
        sku_number, counts = ledger
        print(sku_number, " : ", validate_sku_number(sku_number))