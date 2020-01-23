import re


def multi_re_find(patterns, phrase):
    """
    Takes in a list of regex patterns
    Prints a list of all matches
    """
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' % (pattern))
        print(re.findall(pattern, phrase))
        print('\n')


test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',    # either s or d
                 's[sd]+']   # s followed by one or more s or d

multi_re_find(test_patterns,test_phrase)