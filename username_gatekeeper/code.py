import re

def validate_username(username):
    # Username validation pattern
    pattern = r"^[a-zA-Z0-9]{5,15}$"
    # Forbidden word
    forbidden = "admin"
    if (re.match(pattern, username)and username != forbidden):
        return True
    
    return False


print("12345: ", validate_username("12345")) # True
print("test.username: ", validate_username("test.username")) # False
print("username: ", validate_username("username")) # True
print("hello, world: ", validate_username("hello, world")) # False
print("user0123: ", validate_username("user0123")) # True
print("_user: ", validate_username("_user")) # False
print("user0123456user: ", validate_username("user0123456user")) # True