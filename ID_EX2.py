"""
Itai Dvir
Recursive exercise program
"""


def multiple(a, b):
    """
    get two numbers (a,b). the function returns number a
    times number b after a recursive process.
    """
    rv = 0
    if a == 1:
        rv = b
    else:
        rv = multiple(a - 1, b) + b
    return rv


def power(a, b):
    """
    get two numbers (a,b). the function returns
    number a powered number b times after a recursive process.
    """
    rv = 0
    if (b == 1):
        rv = a
    else:
        rv = power(a, b - 1) * a
    return rv


def divide(a, b):
    """
    get two numbers (a,b). the function returns
    number a devided by number b in a recursive
    process.
    """
    rv = 0
    if (a >= b):
        rv = 1 + divide(a - b, b)
    return rv


def modulo_10(num):
    """
    get num. function returns num moduled
    by 10 in a recursive process.
    """
    if (num > 9):
        num = modulo_10(num - 10)
    return num


def modulo_n(num, n):
    """
    get num and n. function returns num moduled
    by n in a recursive process.
    """
    if (num > n - 1):
        num = modulo_n(num - n, n)
    return num


def stars_length(num):
    """
    get num. function prints stars according
    to the amount of digits the number has.
    """
    if (num > 9):
        stars_length(num / 10)
    print("*", end="")


def stars(num):
    """
    get num. function prints stars according
    to the numbers itself.
    For example: 6 will print '******'
    """
    if (num != 1):
        stars(num - 1)
    print("*", end="")


def triangleUpSideDown(num):
    """
    get num. function prints '*'s in
    a form of an upside down traingle with
    the number of lines same as "num".
    """
    if (num == 1):
        print("*")
    else:
        for i in range(0, num):
            print("*", end="")
        print("")
        triangleUpSideDown(num - 1)


def triangle(num):
    """
    get num. function prints '*'s in
    a form of a traingle with
    the number of lines same as "num".
    """
    if (num != 1):
        triangle(num - 1)
    for i in range(0, num):
        print("*", end="")
    print("")


def reverse_number(num):
    """
    get num. function prints num
    but with the digits reversed.
    """
    if (num <= 9):
        print(num, end="")
    else:
        print(num % 10, end="")
        reverse_number(num // 10)


def repeat_number(num):
    """
    get num. function prints num
    with the digits in order.
    """
    if (num <= 9):
        print(num, end="")
    else:
        firstDigit = num // 10
        count = 10
        while (firstDigit > 9):
            firstDigit //= 10
            count *= 10
        num -= count * firstDigit
        print(firstDigit, end="")
        repeat_number(num)
