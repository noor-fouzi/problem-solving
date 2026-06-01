### 🚀 Problem 10: The API Gateway Rate-Limiter Log
**Level:** Hard (Week 3 Standard)

**Scenario:** Security parameters track traffic flooding by monitoring incoming microservice endpoints. If an application instance sends too many requests in a single hour window, it gets flagged for suspicious activity.

You are given an raw, unsorted traffic report dataset.

#### The Threshold Matrix:
```Python
# Maximum requests allowed per endpoint type per hour
RATE_LIMITS = {
    "/login": 5,
    "/checkout": 10,
    "/search": 20
}
```
#### The Input Stream:

```Python
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
```

### 📋 System Requirements
Write an analytical tracking engine that compiles a dictionary tracking **only the specific IP addresses that breached the security threshold guidelines**.

### Your Strict Architectural Constraints:
1. **The Discovery Map:** You must dynamically track how many requests *each individual IP* makes to *each unique endpoint*. (Hint: This will require initializing a nested structure tracking `hits`).
2. **The Security Guardrail:** If a log entry contains an endpoint that does **not** exist in the `RATE_LIMITS` matrix (such as `"/banned_admin_route"`), print a console warning and skip it entirely.
3. **The Isolation Filter:** The final returned payload dictionary must **only** contain records where an IP's hit count for a specific endpoint strictly **exceeded** ($>$) the maximum allowed limit defined in `RATE_LIMITS`. If an IP stayed within limits, it must not appear in the final output.

### 🎯 Expected Target Output Layout
```Python
{
    "192.168.1.1": [
        {
            "offending_endpoint": "/login",
            "total_hits": 6,
            "allowed_limit": 5
        },
        {
            "offending_endpoint": "/checkout",
            "total_hits": 12,
            "allowed_limit": 10
        }
    ]
}
```