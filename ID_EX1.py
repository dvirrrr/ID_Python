"""
Itai Dvir
Age calculator and name print
"""


def main():
    """
    get birth year and name from user and print
    the name and age.
    """
    name = input("enter your name ")
    birth_year = int(input("enter your birth year "))
    age = (2024 - birth_year)
    print(f"Hello {name}. You are {age} years old.")


if __name__ == '__main__':
    main()