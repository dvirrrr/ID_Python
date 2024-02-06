# Itai Dvir, 20240113

def write_to_file(filename, text):
    try:
            with open(filename, 'w') as file_handle:
                file_handle.write(f"{text}")
    except Exception as e:
        print(f"Error writing to file: {e}")


def read_from_file(filename):
    try:
        file_handle = open(filename, "r")
        text = file_handle.read()
        print(text)
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

