s = "aaaabbbbbcvvvva"


def rle(s):
    res = []
    counter = 1

    for index in range(1, len(s)):
        if s[index] == s[index - 1]:
            counter += 1
        else:
            res.append(f"{s[index - 1]}{counter}")
            counter = 1
    res.append(f"{s[- 1]}{counter}")

    return "".join(res)


def decode_rle(encoded_string):
    res = []
    i = 0

    while i < (len(encoded_string)):
        my_int = int(encoded_string[i + 1])
        char = encoded_string[i]
        res.append(char * my_int)
        i += 2
    return res


print(decode_rle(rle(s)))
print(rle(s))
