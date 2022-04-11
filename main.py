# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas


# def print_hi(name):


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = [-1, 1, 1, 1, -1, 1, 1]
    print("Mode of List A is % s" % (max(set(A), key=A.count)))
    B = ['Hi', 10, 50, 'Hi', 100, 10, 'Hi']
    print("Mode of List B is % s" % (max(set(B), key=B.count)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
