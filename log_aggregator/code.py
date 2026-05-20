def aggregate_logs(web_logs, mobile_logs):
    pass



if __name__ == "__main__":
    # Structure: Contains 'session_id', 'user', and 'status'
    web_logs = [
        {"session_id": "W-901", "user": "noorfouzi", "status": "success"},
        {"session_id": "W-902", "user": "admin", "status": "failed"},
        {"session_id": "W-903", "user": "hacker_joe", "status": "failed"},
        {"session_id": "W-904", "user": "validUser123", "status": "success"},
        {"session_id": "W-905", "user": "noorfouzi", "status": "success"},
        {"session_id": "W-906", "user": "validUser123", "status": "failed"},
    ]

    # Structure: Position-dependent (device_id, user_string, numeric_status_code)
    mobile_logs = [
        ("M-44", "noorfouzi", 200),
        ("M-45", "guest_user", 401),
        ("M-46", "admin", 403),
        ("M-47", "validUser123", 200),
        ("M-48", "guest_user", 401),
    ]