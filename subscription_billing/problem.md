## 🛠️ Problem 09: The Tiered Subscription Billing Engine
**Level:** Hard 

**(Week 3 Standard)Scenario:** A SaaS platform bills users based on their subscription tier and usage metrics. At the end of the month, the billing script must compute the raw invoice cost for each user.

**The Rule Matrix**:

```Python 
# The base monthly cost for having an active account in a tier
TIER_BASE_COSTS = {
    "Free": 0.0,
    "Pro": 29.0,
    "Enterprise": 199.0
}

# Every tier includes a free allowance of API requests.
# If a user exceeds their allowance, they are billed an overage fee per extra request.
TIER_LIMITS = {
    "Free": {"allowed_requests": 1000, "overage_fee_per_request": 0.05},
    "Pro": {"allowed_requests": 50000, "overage_fee_per_request": 0.01},
    "Enterprise": {"allowed_requests": 1000000, "overage_fee_per_request": 0.00}
}
```

**The Input Stream:**

```Python
# Active customer usage database dump
customer_usage = [
    {"customer_id": "C-801", "name": "Alice Barker", "tier": "Free", "monthly_api_requests": 1200},   # Exceeds allowance!
    {"customer_id": "C-802", "name": "DevCorp LLC", "tier": "Enterprise", "monthly_api_requests": 850000}, # Within allowance
    {"customer_id": "C-803", "name": "FinTech Solution", "tier": "Pro", "monthly_api_requests": 55000}, # Exceeds allowance!
    {"customer_id": "C-804", "name": "Charlie Smith", "tier": "Free", "monthly_api_requests": 450},    # Within allowance
    {"customer_id": "C-805", "name": "Banned Hacker", "tier": "Premium_Plus", "monthly_api_requests": 999999} # Corrupt/Invalid Tier!
]
```

### 📋 System Requirements
Write a core calculation engine that aggregates usage data and computes the definitive invoice summary dictionary.

### Your Strict Architectural Constraints:
1. The Invoice Formula:
$$\text{Total Invoice} = \text{Base Tier Cost} + \left( \max(0, \text{Requests Used} - \text{Allowed Requests}) \times \text{Overage Fee} \right)$$

2. **Defensive Tier Guardrail:** If a customer's profile lists a subscription tier that does **not** exist in your rule matrix matrices (such as `"Premium_Plus"`), your system must flag it by printing a warning message to the console and **skipping that customer entirely** without crashing.

3. **Precision Constraint:** Financial payouts must look completely pristine. All calculated invoice numbers must be floats rounded precisely to **2 decimal places**.

### 🎯 Expected Target Output Layout
```Python
{
    "C-801": {
        "name": "Alice Barker",
        "tier": "Free",
        "invoice_amount_usd": 10.00  # Base 0.0 + (200 extra requests * 0.05)
    },
    "C-802": {
        "name": "DevCorp LLC",
        "tier": "Enterprise",
        "invoice_amount_usd": 199.00 # Base 199.0 + (0 extra requests)
    },
    "C-803": {
        "name": "FinTech Solution",
        "tier": "Pro",
        "invoice_amount_usd": 79.00  # Base 29.0 + (5000 extra requests * 0.01)
    },
    "C-804": {
        "name": "Charlie Smith",
        "tier": "Free",
        "invoice_amount_usd": 0.00   # Base 0.0 + (0 extra requests)
    }
}
```