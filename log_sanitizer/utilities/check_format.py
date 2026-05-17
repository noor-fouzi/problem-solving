from split_string import split_string
from clear_spaces import clear_spaces
import re

def is_well_formatted(string):
    splited = split_string(clear_spaces(string), "|")
    if len(splited) == 3:
        if re.match(r"^[0-9]{3}$", splited[2]):
            return True
    
    return False


if __name__ == "__main__":
    print(is_well_formatted("2026-05-17 05:00:12 | noorfouzi | 200"))
    print(is_well_formatted("MALFORMED_LINE_ERR_909"))