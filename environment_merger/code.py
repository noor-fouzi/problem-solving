def environment_merger():
    pass


if __name__ == "__main__":
    # The Default Base Configuration Environment Blueprint
    base_config = {
        "browser": "Chrome",
        "headless": False,
        "timeout_seconds": 30,
        "retry_attempts": 3,
        "reporter": "HTML"
    }

    # The Runtime Environment Overrides Stream (Mixed Types!)
    # Some records are dictionaries, others are position-dependent tuples
    runtime_overrides = [
        {"key": "headless", "value": True},                     # Dict override
        ("timeout_seconds", 45),                                # Tuple override
        {"key": "retry_attempts", "value": 5},                  # Dict override
        ("network_emulation", "4G_Throttled"),                  # New setting tuple!
        {"key": "unknown_flag", "value": "ignored"},            # BANNED key! Filter out.
        ("experimental_mode", True)                             # New setting tuple!
    ]

    base_config.update(dict(
        network_emulation = "4G_Throttled"
    ))

    print(base_config)