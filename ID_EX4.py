"""
Itai Dvir
String exercise
"""


# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
    """
    get count. function returns 'many' if count
    equals or more than 10 or the number as a
    string if not.
    """
    d_line = "Number of donuts: "
    if count >= 10:
        return d_line + 'many'
    else:
        return d_line + str(count)


# B. both_ends
# Given a string my_input, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(my_input):
    """
    get my_input. function returns the first
    two and last two characters in a new
    string, or if my_input is smaller than 2,
    it returns a blank string.
    """
    length = len(my_input)
    new_str = ''
    if length > 2:
        new_str += my_input[0]
        new_str += my_input[1]
        new_str += my_input[-2]
        new_str += my_input[-1]
    elif length == 2:
        new_str = my_input
    return new_str


# C. fix_start
# Given a string my_input, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(my_input):
    """
    get my_input. function returns a string
    that doesn't have the first char again
    unless it is replaced by char '*'
    """
    length = len(my_input)
    new_str = ''
    k_char = '*'
    first_char = my_input[0]
    new_str += first_char
    for i in range(1, length):
        current_char = my_input[i]
        if current_char == first_char:
            new_str += k_char
        else:
            new_str += current_char

    return new_str


# D. MixUp
# Given strings input1 and input2, return a single string with input1 and
# input2 separated by a space '<input1> <input2>',
# except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(input1, input2):
    """
    get input1 and input2, function returns
    a longer string with input1 added to input2
    with a space in-between, but the first and
    second chars in these two strings
    are swapped for one another.
    """
    replace_for1 = input2[:2]
    continuation_for1 = input1[2:]
    replace_for2 = input1[:2]
    continuation_for2 = input2[2:]
    new1 = replace_for1 + continuation_for1
    new2 = replace_for2 + continuation_for2
    new_str = new1 + " " + new2
    return new_str


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

    print('\ndonuts')
    # Each line calls donuts, compares its result to the expected result
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print('\nboth_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print('\nfix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print('\nmix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
