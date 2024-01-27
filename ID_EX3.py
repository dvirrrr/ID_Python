"""
Itai Dvir
Loops training / exercise
"""


def print_in_loop_1_to_40():
    """
    function prints number 1-40 in loop.
    There are 40 lines with each line a number.
    """
    for i in range(1, 41):
        print(i)


def print_in_while_1_to_40():
    """
    function prints number 1-40 in  while loop.
    There are 40 lines with each line a number.
    """
    i = 1
    while (i != 41):
        print(i)
        i += 1


def boom():
    """
    function loops 1-100 and only prints
    numbers that are integer numbers when
    devided by 7.
    """
    for i in range(0, 101):
        if ((i % 7 == 0) | (i % 10 == 7) | (i // 10 == 7) | (i == 0)):
            print(i)


def fib():
    """
    function prints all fibornachi numbers
    as long as they are smaller than 10000
    """
    a = 0
    b = 1
    print(a)
    while (a + b < 10000):
        print(f"{a + b}")
        a = a + b
        b = a - b


def print_dec():
    """
    function prints roundly if num is intengable
    or as float if number is not round.
    """
    num = 0.0
    while (num <= 5):
        if (num.is_integer()):
            print(int(num))
        else:
            print(num)
        num = round(num + 0.1, 1)
