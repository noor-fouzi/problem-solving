def aggregate_logs(web_logs, mobile_logs):
    
    aggregator = {}

    for log in web_logs:
        user = log.get("user")
        if user not in aggregator:
            aggregator.update({
                user : dict(
                    web_sessions = [],
                    mobile_devices = [],
                    total_successful_logins = 0
                )
            })

        
        aggregator[user]["web_sessions"].append(log.get("session_id"))
        if log.get("status") == "success":
            aggregator[user]["total_successful_logins"] += 1

    for log in mobile_logs:
        device, user, status_code = log
        if user not in aggregator:
            aggregator.update({
                user: dict(
                    web_sessions = [],
                    mobile_devices = [],
                    total_successful_logins = 0
                )
            })

        aggregator[user]["mobile_devices"].append(device)
        if status_code == 200:
            aggregator[user]["total_successful_logins"] += 1

    return aggregator
        

if __name__ == "__main__":

    web_logs = [
        {"session_id": "W-901", "user": "noorfouzi", "status": "success"},
        {"session_id": "W-902", "user": "admin", "status": "failed"},
        {"session_id": "W-903", "user": "hacker_joe", "status": "failed"},
        {"session_id": "W-904", "user": "validUser123", "status": "success"},
        {"session_id": "W-905", "user": "noorfouzi", "status": "success"},
        {"session_id": "W-906", "user": "validUser123", "status": "failed"},
    ]

    mobile_logs = [
        ("M-44", "noorfouzi", 200),
        ("M-45", "guest_user", 401),
        ("M-46", "admin", 403),
        ("M-47", "validUser123", 200),
        ("M-48", "guest_user", 401),
    ]

    print(aggregate_logs(web_logs, mobile_logs))