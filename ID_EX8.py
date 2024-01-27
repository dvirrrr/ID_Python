# Itai Dvir, 20240113

def write_to_file():
    try:
        words = ["hi", "everyone"]
        with open('readme.txt', 'w') as file_handle:
            for word in words:
                file_handle.write(f"{word}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")


def read_from_file():
    try:
        with open('readme.txt') as file_handle:
            lines = file_handle.readlines()
            for line in lines:
                print(line)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error reading from file: {e}")


def front_x(words):
    try:
        starting_with_x = []
        not_starting_with_x = []
        for word in words:
            if word.startswith('x'):
                starting_with_x.append(word)
            else:
                not_starting_with_x.append(word)
        rv = sorted(starting_with_x) + sorted(not_starting_with_x)
        return rv
    except Exception as e:
        print(f"Error in front_x function: {e}")


def sqrt(number):
    """
    get number, return square root of number
    """
    try:
        assert type(number) == int or type(number) == float, "Please enter a number"
        assert number >= 0, "Please enter a non-negative number"
        return number ** 0.5
    except AssertionError as e:
        print(e)
        return None

def main():
    try:
        write_to_file()
        read_from_file()
        print(sqrt(182))
        sqrt('ro')
    except Exception as e:
        print(f"Error in main function: {e}")


if __name__ == "__main__":
    main()

