def clear_spaces(string):
    clear = ""
    for character in string:
        if character == ' ':
            continue

        clear += character

    return clear


if __name__ == "__main__":
    print(clear_spaces(" hell o"))
    print(clear_spaces("this is a sentence ."))