# s = "aaaaaabbbbbccca"
# s = "000011112225"
s = ""


def rle_encode(s):
    if not s:
        return s

    res = []
    counter = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            counter += 1
        else:
            res.extend([str(counter), str(s[i-1])])
            counter = 1
    res.extend([str(counter), str(s[-1])])
    return ''.join(res)


print(rle_encode(s))
