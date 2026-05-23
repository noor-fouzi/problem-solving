def environment_merger(base_config, config_updates):

    white_list = {"browser", "headless", "timeout_seconds", "retry_attempts", "reporter", "network_emulation", "experimental_mode"}

    for update in config_updates:
        if type(update) == dict:
            key = update.get("key")
            if key in white_list:
                base_config.update({
                    key: update.get("value")
                })

        elif type(update) == tuple:
            key, value = update
            print(key, value)
            if key in white_list:
                base_config.update({
                    key: value
                })

    return base_config


if __name__ == "__main__":
    base_config = {
        "browser": "Chrome",
        "headless": False,
        "timeout_seconds": 30,
        "retry_attempts": 3,
        "reporter": "HTML"
    }

    runtime_overrides = [
        {"key": "headless", "value": True},                     # Dict override
        ("timeout_seconds", 45),                                # Tuple override
        {"key": "retry_attempts", "value": 5},                  # Dict override
        ("network_emulation", "4G_Throttled"),                  # New setting tuple!
        {"key": "unknown_flag", "value": "ignored"},            # BANNED key! Filter out.
        ("experimental_mode", True),                            # New setting tuple!
        "Unknown Configuration"
    ]

    print(environment_merger(base_config, runtime_overrides))