from clear_spaces import clear_spaces

def split_string(string, split_char = ' '):
    splited_string = []
    holder = ""
    for character in range (len(string)):

        if string[character] == split_char or  character == len(string):
            splited_string.append(clear_spaces(holder))
            holder = ""
        else:
            holder += string[character]

    splited_string.append(holder)
    return splited_string

if __name__ == "__main__":
    print(split_string("hello", " "))
    print(split_string("timestamp | username | statuscode", "|"))
    print(split_string("You&Me", "&"))