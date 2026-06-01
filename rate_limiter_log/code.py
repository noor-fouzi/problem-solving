from dct_to_set import dct_to_set
from get_ips import get_ips
from hit_count import endpoints_hit_count

def rate_limiter(gateway_logs):

    # Maximum requests allowed per endpoint type per hour
    RATE_LIMITS = {
        "/login": 5,
        "/checkout": 10,
        "/search": 20
    }

    exceeded_limits = {}
    endpoints_count = endpoints_hit_count(gateway_logs)
    whitelist = dct_to_set(RATE_LIMITS)

    for ip in endpoints_count:

        for endpoint in endpoints_count[ip]:
            if endpoint in whitelist:
                
                hits_number = endpoints_count[ip][endpoint]
                if hits_number > RATE_LIMITS[endpoint]:

                    if ip not in exceeded_limits:
                        exceeded_limits.update({
                            ip : []
                        })

                    exceeded_limits[ip].append({
                        "offending_endpoint": endpoint,
                        "total_hits": hits_number,
                        "allowed_limit": RATE_LIMITS[endpoint]
                    })

    return exceeded_limits


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