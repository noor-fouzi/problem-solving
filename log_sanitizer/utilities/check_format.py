from split_string import split_string
import re

def is_well_formatted(string):
    splited = split_string(string)
    return len(splited) == 3 and re.match(r"^[0-5]{3}$", splited[2])


if __name__ == "__main__":
    print(is_well_formatted("2026-05-17 05:00:12 | noorfouzi | 200"))
    print(is_well_formatted("MALFORMED_LINE_ERR_909"))