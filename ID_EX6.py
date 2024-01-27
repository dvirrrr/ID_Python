# Amir Shahal, 20231227

def write_to_file(filename, text):
    """
    get a file path and text, function
    creates a text file in path if not
    already created and writes 'text' to it.
    """
    file_handle = open(filename, 'w')
    file_handle.write(f"{text}")


def read_from_file(filename):
    """
    get a file path, function prints file text's
    text.
    """
    file_handle = open(filename, "r")
    text = file_handle.read()
    print(text)

def read_3_lines(filename):
    """
    get a file path, fucntion prints file text's
    first three lines (or less)
    """
    file_handle = open(filename, "r")
    for line in file_handle.readlines()[:3]:
        print(line, end="")

def copy_paste(fp1, fp2):
    """
    get 2 file paths, function copies from
    file path 1 a text file and pastes in
    file path 2.
    """
    with open(fp1, "r") as file_handler:
        text = file_handler.read()
    with open(fp2, "w") as file_handler2:
        file_handler2.write(text)

def front_x(words):
    starting_with_x = []
    not_starting_with_x = []
    for word in words:
        if word.startswith('x'):
            starting_with_x.append(word)
        else:
            not_starting_with_x.append(word)
    rv = sorted(starting_with_x) + sorted(not_starting_with_x)
    return rv


def main():
    write_to_file(r"C:\PythonWork\Bina\fileText.txt", "Blocked by james!")
    read_from_file(r"C:\PythonWork\Bina\fileText.txt")
    #read_3_lines(r"C:\PythonWork\Bina\fileText.txt")
    #copy_paste(r"C:\PythonWork\Bina\fileText.txt", r"C:\PythonWork\Bina2")



if __name__ == "__main__":
    main()
