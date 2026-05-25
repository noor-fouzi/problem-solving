from dct_to_set import dct_to_set

def subscriptions_billing(customer_usage):

    TIER_BASE_COSTS = {
        "Free": 0.0,
        "Pro": 29.0,
        "Enterprise": 199.0
    }
    
    TIER_LIMITS = {
        "Free": {"allowed_requests": 1000, "overage_fee_per_request": 0.05},
        "Pro": {"allowed_requests": 50000, "overage_fee_per_request": 0.01},
        "Enterprise": {"allowed_requests": 1000000, "overage_fee_per_request": 0.00}
    }

    whitelist = dct_to_set(TIER_BASE_COSTS)

    billing_summary = {}

    for usage in customer_usage:
        tier = usage.get("tier")
        if tier in whitelist:
            customer_id = usage.get("customer_id")
            if customer_id not in billing_summary:
                billing_summary.update({
                    customer_id: dict(
                        name = usage.get("name"),
                        tier = tier,
                        invoice_amount_usd = 0
                    )
                })
            
                usage_overage = usage.get("monthly_api_requests") - TIER_LIMITS[tier]["allowed_requests"]
                fees = 0
                if usage_overage <= 0:
                    fees += TIER_BASE_COSTS[tier]
                
                else: 
                    fees += TIER_BASE_COSTS[tier] + (usage_overage * TIER_LIMITS[tier]["overage_fee_per_request"])

                billing_summary[customer_id]["invoice_amount_usd"] = f"{fees:.2f}"

        else:
            print("Warning: Invalid tier!")


    return billing_summary


if __name__ == "__main__":
    customer_usage = [
        {"customer_id": "C-801", "name": "Alice Barker", "tier": "Free", "monthly_api_requests": 1200},   # Exceeds allowance!
        {"customer_id": "C-802", "name": "DevCorp LLC", "tier": "Enterprise", "monthly_api_requests": 850000}, # Within allowance
        {"customer_id": "C-803", "name": "FinTech Solution", "tier": "Pro", "monthly_api_requests": 55000}, # Exceeds allowance!
        {"customer_id": "C-804", "name": "Charlie Smith", "tier": "Free", "monthly_api_requests": 450},    # Within allowance
        {"customer_id": "C-805", "name": "Banned Hacker", "tier": "Premium_Plus", "monthly_api_requests": 999999} # Corrupt/Invalid Tier!
    ]
    
    print(subscriptions_billing(customer_usage))