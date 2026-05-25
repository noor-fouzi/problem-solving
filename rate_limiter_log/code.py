def rate_limiter(gateway_logs):
    pass


if __name__ == "__main__":
    # Raw API traffic access logs
    gateway_logs = [
        {"ip": "192.168.1.1", "endpoint": "/login", "status": "200"},
        {"ip": "10.0.0.5", "endpoint": "/search", "status": "200"},
        {"ip": "192.168.1.1", "endpoint": "/login", "status": "401"},
        {"ip": "192.168.1.1", "endpoint": "/login", "status": "200"},
        {"ip": "10.0.0.5", "endpoint": "/checkout", "status": "200"},
        {"ip": "192.168.1.1", "endpoint": "/login", "status": "200"},
        {"ip": "192.168.1.1", "endpoint": "/login", "status": "401"},
        {"ip": "192.168.1.1", "endpoint": "/login", "status": "200"}, # 6th request for this IP on /login! Limit exceeded!
        {"ip": "10.0.0.5", "endpoint": "/banned_admin_route", "status": "404"} # Missing endpoint from limits matrix!
    ]

    print(rate_limiter(gateway_logs))