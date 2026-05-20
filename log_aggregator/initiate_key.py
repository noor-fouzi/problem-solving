def initiate_key(ky, dct):
    if ky not in dct:
        dct.update(
            {
                ky: dict(

                    web_sessions = [],
                    mobile_devices = [],
                    total_successful_logins = 0

                )
            }
        )


if __name__ == "__main__":
    dct = {}
    ky = "user"
    initiate_key(ky, dct)
    print(dct)