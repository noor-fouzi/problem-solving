def tuple_to_dictionary(tpl):
    user_id, billing_tier, is_active = tpl
    return {
            user_id: dict(
                tier = billing_tier,
                is_active = is_active
        )}


if __name__ == "__main__":
    billing_records = [
        (101, "Premium", True),
        (102, "Basic", True),
        (103, "Premium", False), # Suspended account!
        (104, "Enterprise", True)
    ]

    for tpl in billing_records:
        print(tuple_to_dictionary(tpl))