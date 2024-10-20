# Y Nhi Tran
# Exercise Recursion

import os


def print_file_list(file_list):
    for file in file_list:
        if os.path.isdir(file):
            print_file_list(os.listdir(file))
        else:
            print(file)


def fileList():
    return os.listdir()


def recursive_print_files():
    file_list = fileList()
    print_file_list(file_list)


# Call the recursivePrintFiles function
recursive_print_files()
