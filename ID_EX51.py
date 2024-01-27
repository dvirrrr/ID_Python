"""
Itai Dvir
list exercise 1
"""


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    """
    get list words. function returns a
    count for how many string in the list
    have the same first char as the last and
    if the string is longer than 2 characters.
    """
    listLength = len(words)
    count = 0
    for i in range(0, listLength):
        if (words[i] != ''):
            firstAndLast = words[i][0] == words[i][-1]
            if (len(words[i]) >= 2) & (firstAndLast):
                count += 1
    return count


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    """
    get list words, function return a resorted list
    but words with the initial 'x' go first, than it
    goes by the rest of the abc.
    """
    listLength = len(words)
    x_list = list()
    other_words = list()
    for i in range(0, listLength):
        if (words[i][0] == 'x'):
            x_list.insert(i, words[i])
        else:
            other_words.insert(i, words[i])
    x_list.sort()
    other_words.sort()
    sorted_list = x_list + other_words
    return sorted_list


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    """
    makes a list consisting new tuples (tuples_sorter),
    each having current_tuple[-1] which is the last
    number in each tuple, and current_tuple
    which is straight up the tuple in this place,
    "for current_tuples in tuples"
    means in the range of tuples' length.
    and current_tuples is like variable 'i' in loops.
    then you sort them by basically current_tuples[-1].
    then, you create another list sorted_tuples
    which goes for this 'i' like variable 'current_tuple'
    in the range of 'tuples_sorter'.
    """
    tuples_length = len(tuples)
    tuples_sorter = [(current_tuple[-1], current_tuple) for current_tuple in tuples]
    tuples_sorter.sort()

    sorted_tuples = [current_tuple for unused_variable, current_tuple in tuples_sorter]
    return sorted_tuples


def test(got, expected):
    """ simple test() function used in main() to print
        what each function returns vs. what it's supposed to return. """

    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    """ main() calls the above functions with interesting inputs,
        using test() to check if each result is correct or not. """

    print('\nmatch_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('\nfront_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('\nsort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
