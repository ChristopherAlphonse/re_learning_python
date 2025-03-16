def is_balanced(code):
    # Step 1: Create a frequency dictionary for characters
    # freq_dict will store the frequency of each character in the string 'code'
    freq_dict = {}
    for char in code:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Step 2: Create a frequency of frequencies dictionary
    # frequency_count will store how many times each frequency occurs
    frequency_count = {}
    for val in freq_dict.values():
        if val in frequency_count:
            frequency_count[val] += 1
        else:
            frequency_count[val] = 1

    # dict_length stores the number of unique frequencies
    dict_length = len(frequency_count)

    # If there are 3 or more different frequencies, it's impossible to balance by removing one character
    if dict_length >= 3:
        return False

    # If there's only one unique frequency
    if dict_length == 1:
        # Check if all characters are the same or if the frequency is 1, which is a special case
        if len(freq_dict.keys()) == 1:
            return True
        # If all characters have the same frequency, we can remove one to potentially balance the string
        return list(frequency_count.keys())[0] == 1

    # If there are exactly two unique frequencies
    for val, freq in frequency_count.items():
        # Check if one of the frequencies is 1 and it occurs exactly once, allowing removal to balance the string
        if val == 1 and freq == 1:
            return True

    # Extract the two unique frequencies for further checks
    values = list(frequency_count.keys())

    # Check if the difference between the two frequencies is 1 and the higher frequency occurs exactly once
    if values[0] - values[1] == 1 and frequency_count[values[0]] == 1:
        return True

    # Check the reverse of the above condition
    if values[1] - values[0] == 1 and frequency_count[values[1]] == 1:
        return True

    # If none of the conditions are met, it's impossible to balance by removing one character
    return False


# Example usage
print(is_balanced("arghh"))
print(is_balanced("haha"))
print(is_balanced("aaaabb"))


# not my solution need to revise
