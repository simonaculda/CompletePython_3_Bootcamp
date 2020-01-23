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


test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]


multi_re_find(test_patterns,test_phrase)
