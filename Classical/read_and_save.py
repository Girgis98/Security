import os


def read(path):
    file1 = open(path, "r")
    input = file1.readlines()
    file1.close()
    return input


def write(path, output):
    file1 = open(path, "a")
    file1.write(output)
    file1.close()
    return 1

