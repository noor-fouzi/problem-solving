import re

def validate_username(username):
    # Username validation pattern
    pattern = r"^[a-zA-Z0-9]{5,15}$"
    # Forbidden word
    forbidden = "admin"
    if (re.match(pattern, username)and username != forbidden):
        return True
    
    return False