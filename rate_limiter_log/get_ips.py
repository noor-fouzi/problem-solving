def get_ips(logs):

    ips = []

    for log in logs:
        ips.append(log)

    return ips

if __name__ == "__main__":

    gateway_logs = {
        '192.168.1.1': {'/login': 6}, 
        '10.0.0.5': {'/search': 1, '/checkout': 1, '/banned_admin_route': 1}
    }
    print(get_ips(gateway_logs))