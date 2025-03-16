# Problem 2: Pirate Message Check
# Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

from collections import defaultdict


def can_trust_message(message):
    message_str = message.lower()

    my_map = defaultdict(int)
    for el in message_str:
        my_map[el] += 1

    return sum(my_map.values()) >= 26


message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))


# True
# False
