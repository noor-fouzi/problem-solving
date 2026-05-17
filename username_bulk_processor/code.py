import sys, os

parent_dirctory = os.path.abspath( # Turn it into an absolute path
    os.path.join( 
        os.path.dirname(__file__), # Parent directory of curent file
        '..' # Go up one level in directories tree 
    )
)

# Add to search perimeter of python import
if parent_dirctory not in sys.path:
    sys.path.append(parent_dirctory)

from username_gatekeeper.code import validate_username


def process_signups(usernames_list):

    valid_usernames_count = 0
    invalid_usernames_count = 0
    invalid_usernames = []

    if len(usernames_list) > 0:
        for username in usernames_list:
            if validate_username(username):
                valid_usernames_count += 1
            else:
                invalid_usernames_count += 1
                invalid_usernames.append(username)
    else:
        print("We can't process an empty list!")

    return dict(
        successful_count = valid_usernames_count,
        failed_count = invalid_usernames_count,
        rejected_usernames =  invalid_usernames
    )

if __name__ == "__main__":
    print(process_signups([])) 
    # >> We can't process an empty list!

    print(process_signups(["AdMiN", "User", "Username", "user_name"]))
    # >> {
    #       'successful_count': 1,
    #       'failed_count' : 3,
    #       'invalid_usernames': ['AdMiN', 'User', 'user_name']
    # }

    print(process_signups(["010101", "USERNAME", "ohayohelloworld"]))
    # >> {
    #       'successful_count': 3,
    #       'failed_count' : 0,
    #       'invalid_usernames': []
    # }

    print(process_signups(["helloworldIamhere", "user name", "1+1=2"]))
    # >> {
    #       'successful_count': 0,
    #       'failed_count' : 3,
    #       'invalid_usernames': ['helloworldIamhere', 'user name', '1+1=2']
    # }