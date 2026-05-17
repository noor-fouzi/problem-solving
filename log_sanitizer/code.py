import os, sys

utilities_directory = os.path.abspath(
    os.path.join(
            os.path.dirname(__file__), "./utilities"
    )
)

parent_dirctory = os.path.abspath( 
    os.path.join( 
        os.path.dirname(__file__), 
        '..'
    )
)

if parent_dirctory not in sys.path:
    sys.path.append(parent_dirctory)

if utilities_directory not in sys.path:
    sys.path.append(utilities_directory)

from username_gatekeeper.code import validate_username
from check_format import is_well_formatted
from split_string import split_string
from clear_spaces import clear_spaces


def filter_logs(login_logs):
    
    successful_attempts = []
    failed_attempts = []

    for log in login_logs:

        if is_well_formatted(log):
            splited = split_string(log, "|")

            if clear_spaces(splited[2]) == "200":
                username = clear_spaces(splited[1])
                if validate_username(username):
                    successful_attempts.append(username)

            else:
                failed_attempts.append(clear_spaces(splited[1]))

        else:
            continue

    return dict(
        secure_events = successful_attempts,
        flagged_attempts = failed_attempts
    )



if __name__ == "__main__":
    raw_logs = [
        "2026-05-17 05:00:12 | noorfouzi | 200",
        "2026-05-17 05:01:45 | admin | 403",
        "MALFORMED_LINE_ERR_909",
        "2026-05-17 05:03:22 | hacker_joe | 403",
        "2026-05-17 05:04:11 | validUser123 | 200",
        "| | 200"
    ]

    print(filter_logs(raw_logs))
    # >> {
    #       'secure_events':['noorfouzi', 'validUser123'],
    #       'flagged_attempts': ['admin', 'hacker_joe']
    #}