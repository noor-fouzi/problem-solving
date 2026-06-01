def endpoints_hit_count(logs):

    endpoints_count = {}

    for log in logs:
        
        ip = log.get("ip")
        if ip not in endpoints_count:
            endpoints_count.update({
                ip : dict()
        })
            
        endpoint = log.get("endpoint")
        if endpoint not in endpoints_count[ip]:
            endpoints_count[ip].update({
                endpoint : 0
            })
        
        endpoints_count[ip][endpoint] += 1

    return endpoints_count    


if __name__ == "__main__":

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

    print(endpoints_hit_count(gateway_logs))