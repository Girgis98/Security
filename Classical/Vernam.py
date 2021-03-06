import numpy as np
from math import *
from read_and_save import *


def Vernam(text, key):
    dic2 = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
        "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
        "y": 24, "z": 25}
    dic = {
        0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l",
        12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x",
        24: "y", 25: "z"
    }

    # lowercase
    text = text.lower()
    key = key.lower()

    # remove whitespaces
    text = text.replace(" ", "").replace("\n", "")
    key = key.replace(" ", "").replace("\n", "")

    # convert to numbers
    text_ls = []
    key_ls = []
    for i in range(len(text)):
        text_ls.append(dic2[text[i]])
        key_ls.append(dic2[key[i]])

    out = []
    # Encrypt
    for i in range(len(text)):
        out.append((text_ls[i] + key_ls[i]) % 26)

    # convert to letters
    out_str = ""
    for i in range(len(text)):
        out_str = out_str + (dic[out[i]])

    return out_str


# testing
'''
out = Vernam("RAMSWARUPK" , "RANCHOBABA")
print(out)
'''

delete_file_content("D:\Desktop\To Do\security\Projects\Classical\Input Files\Vernam/vernam_cipher.txt")
for line in read("D:\Desktop\To Do\security\Projects\Classical\Input Files\Vernam/vernam_plain.txt"):
    out = Vernam(line, "SPARTANS")
    print(out)
    write("D:\Desktop\To Do\security\Projects\Classical\Input Files\Vernam/vernam_cipher.txt", out)
