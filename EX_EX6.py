def read_from_file(file):
    my_text = open(file, 'r')
    txt = my_text.read()
    my_text.close()
    print(txt)


def write_to_file(file, st):
    my_file = open(file, 'w')
    my_file.write(st)
    my_file.close()


def read_3_lines(file):
    with open(file, 'r') as file:
        for l in range(3):
            line = file.readline()
            if not line:
                break
            print(line, end=" ")


def copy_paste(file1, file2):
    f1 = open(file1, 'rb')
    content = f1.read()
    f1.close()
    f2 = open(file2, 'wb')
    f2.write(content)
    f2.close()


def main():
    write_to_file(r"C:\PythonWork\Bina\fileText.txt", "Blocked by james!")
    read_from_file(r"C:\PythonWork\Bina\fileText.txt")
    read_3_lines(r"C:\PythonWork\Bina\fileText.txt")
    copy_paste(r"C:\PythonWork\Bina\fileText.txt", r"C:\PythonWork\Bina2")



if __name__ == "__main__":
    main()