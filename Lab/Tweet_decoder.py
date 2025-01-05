# The following program decodes a few common abbreviations in online communication such as messages in Twitter ("tweets") or email, and provides the corresponding English phrase.
# tweet = input('Enter abbreviation from tweet:\n')

# if tweet == 'LOL':
#     print('LOL = laughing out loud')
# elif tweet == 'BFN':
#     print('BFN = bye for now')
# elif tweet == 'FTW':
#     print('FTW = for the win')
# elif tweet == 'IRL':
#     print('IRL = in real life')
# else:
#     print("Sorry, don't know that one")


# Create different versions of the program that:

# Expand the number of abbreviations that can be decoded. Add support for abbreviations you commonly use or search the internet for some.
# Allow the user to enter a complete tweet (160 characters or less) as a single line of text. Search the resulting string for abbreviations and print a list of each abbreviation along with its decoded meaning.

abbreviations = {
    'LOL': 'Laugh Out Loud',
    'BFN': 'Bye For Now',
    'FTW': 'For The Win',
    'IRL': 'In Real Life',
    'YOLO': 'You Only Live Once',
    'BRB': 'Be Right Back',
    'SMH': 'Shaking My Head',
    'TMI': 'Too Much Information',
    'IDK': 'I Don\'t Know',
    'DM': 'Direct Message',
    'TBH': 'To Be Honest',
    'BFF': 'Best Friends Forever'
}

search = input('Enter word to be decoded: ').upper()
if len(search) < 1 or len(search)>= 160:
    print("Invalid . search mst be 160 characters or less must be in the range of 1-160.")
elif search in abbreviations:
    print(f"{abbreviations[search]}")
else:
    print("Word not found!")
        
