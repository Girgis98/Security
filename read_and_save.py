import os


def read(path):
    file1 = open(path, "r")
    input = file1.readlines()
    file1.close()
    return input


def write(path, output):
    file1 = open(path, "a")
    file1.write(output + "\n")
    file1.close()
    return 1

def delete_file_content(path):
    file1 = open(path, "w")
    file1.write("")
    file1.close()
    return 1
