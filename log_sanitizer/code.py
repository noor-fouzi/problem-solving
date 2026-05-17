def filter_logs(login_logs):
    pass


if __name__ == "__main__":
    raw_logs = [
        "2026-05-17 05:00:12 | noorfouzi | 200",
        "2026-05-17 05:01:45 | admin | 403",
        "MALFORMED_LINE_ERR_909",
        "2026-05-17 05:03:22 | hacker_joe | 403",
        "2026-05-17 05:04:11 | validUser123 | 200"
    ]

    filter_logs(raw_logs)
    # >> {
    #       'secure_events':['noorfouzi', 'validUser123'],
    #       'flagged_attempts': ['admin', 'hacker_joe']
    #}