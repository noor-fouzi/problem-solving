def subscriptions_billing():
    pass


if __name__ == "__main__":
    customer_usage = [
    {"customer_id": "C-801", "name": "Alice Barker", "tier": "Free", "monthly_api_requests": 1200},   # Exceeds allowance!
    {"customer_id": "C-802", "name": "DevCorp LLC", "tier": "Enterprise", "monthly_api_requests": 850000}, # Within allowance
    {"customer_id": "C-803", "name": "FinTech Solution", "tier": "Pro", "monthly_api_requests": 55000}, # Exceeds allowance!
    {"customer_id": "C-804", "name": "Charlie Smith", "tier": "Free", "monthly_api_requests": 450},    # Within allowance
    {"customer_id": "C-805", "name": "Banned Hacker", "tier": "Premium_Plus", "monthly_api_requests": 999999} # Corrupt/Invalid Tier!
]