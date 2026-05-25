def dct_to_set(dct):

    whitelist = set()

    for key in dct:
        whitelist.add(key)

    return whitelist
    


if __name__ == "__main__":
    TIER_BASE_COSTS = {
        "Free": 0.0,
        "Pro": 29.0,
        "Enterprise": 199.0
    }

    dct_to_set(TIER_BASE_COSTS)