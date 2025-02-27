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


def rle_decode(encoded_string: str) -> str:
    if not encoded_string:
        return encoded_string

    res = []
    i = 0
    while i < len(encoded_string):
        length = int(encoded_string[i])
        char = encoded_string[i + 1]
        res.append(char * length)
        i += 2
    return ''.join(res)


s = "aaaaaabbbbbccca"
encoded_s = rle_encode(s)
print(f"Encoded: {encoded_s}")

decoded_s = rle_decode(encoded_s)
print(f"Decoded: {decoded_s}")
