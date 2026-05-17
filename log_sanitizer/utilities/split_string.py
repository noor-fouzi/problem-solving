def split_string(string, split_char = ' '):
    splited_string = []
    holder = ""
    for character in range (len(string)):

        if string[character] == split_char or  character == len(string):
            splited_string.append(holder)
            holder = ""
        else:
            holder += string[character]
            print(holder)

    splited_string.append(holder)
    return splited_string


print(split_string("hello", " "))