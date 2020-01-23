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


test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters

multi_re_find(test_patterns,test_phrase)