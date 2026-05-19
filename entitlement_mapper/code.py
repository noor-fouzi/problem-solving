from tpl_to_dct import tuple_to_dictionary

def map_user_to_permissions(profiles, subscriptions):
    mapped = {}
    lookup_dictionary = {}
    
    for subscription in subscriptions:
        lookup_dictionary.update(tuple_to_dictionary(subscription))

    for profile in profiles:
        user_id = profile.get('user_id')
        user_subscription = lookup_dictionary.get(user_id)
        
        if user_subscription['is_active']:
            mapped.update({
                user_id: dict(
                    name = profile.get('name'),
                    type = profile.get('type'),
                    tier = user_subscription.get('tier')
                )
            })
    
    return mapped


if __name__ == "__main__":

    user_profiles = [
        {"user_id": 101, "name": "Alpha Corp", "type": "establishment"},
        {"user_id": 102, "name": "Omega Tech Institute", "type": "institute"},
        {"user_id": 103, "name": "Beta Industries", "type": "establishment"},
        {"user_id": 104, "name": "Delta Academy", "type": "institute"}
    ]

    # Format: (user_id, billing_tier, Is_active_boolean)
    billing_records = [
        (101, "Premium", True),
        (102, "Basic", True),
        (103, "Premium", False), # Suspended account!
        (104, "Enterprise", True)
    ]

    print(map_user_to_permissions(user_profiles, billing_records))