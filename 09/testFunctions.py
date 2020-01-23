from functools import reduce


def word_lengths(phrase):
    return list(map(lambda len_w: len(len_w), list(phrase.split())))


# print(word_lengths('How long are the words in this phrase'))


def digits_to_num(digits):

    return reduce(lambda x, y: x*10 + y, digits)


# print(digits_to_num([3,4,3,2,1]))

def filter_words(word_list, letter):

    return list(filter(lambda word: word[0] == letter, word_list))


# l = ['hello','are','cat','dog','ham','hi','go','to','heart']
# print(filter_words(l,'h'))

def concatenate(L1, L2, connector):

    return list(map(lambda item: str(item[0] + connector + item[1]), zip(L1, L2)))
    # return list(zip(lambda x, y: x+connector+y, L1, L2))
    # return list(zip(L1,L2))


# print(concatenate(['A','B'],['a','b'],'-'))

def d_list(L):

    d = {}
    for index, item in enumerate(L):
        d[item] = index
    return d


# print(d_list(['a','b','c']))

def count_match_index(L):
    # l_t = list(enumerate(L))
    # print(l_t)
    # for x, y in l_t:
    #     print(x== y)
    # print (list(map(lambda x: x[0] == x[1], l_t)))

    return len( list(filter(lambda item: item[0] == item[1], list(enumerate(L)))))
    # print(list_m)
    # return len(list_m)

    # for index, item in enumerate(L):
    #     if index == item:



print(count_match_index([0,2,2,1,5,5,6,10]))

