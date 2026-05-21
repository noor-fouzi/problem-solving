def tpl_to_dct(tpl):
    sku_number, count = tpl
    return{
        sku_number: dict(
            ledger_count = count
    )}


if __name__ == "__main__":
    digital_ledger = [
        ("SKU-101", 45),
        ("SKU-102", 15),
        ("SKU-103", 100),
        ("SKU-104", 25),
        ("SKU-106", 50)
    ]

    for ledger in digital_ledger:
        print(tpl_to_dct(ledger))