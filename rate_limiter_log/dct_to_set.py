def dct_to_set(dct):

    keys = set()

    for key in dct:
        keys.add(key)
    
    return keys


if __name__ == "__main__":

    RATE_LIMITS = {
        "/login": 5,
        "/checkout": 10,
        "/search": 20
    }

    print(dct_to_set(RATE_LIMITS))