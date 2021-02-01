import numpy as np
from math import *
from read_and_save import *


def Hill(text, key):
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

    # key as np array
    key = np.array(key)

    # remove whitespaces
    text = text.replace(" ", "").replace("\n", "")

    # add x to end
    while (len(text)) % np.shape(key)[0] > 0:
        text = text + 'x'

    # convert alpha to num
    text_arr = np.zeros((len(text), 1))
    for i, val in enumerate(text):
        text_arr[i] = (dic2[val])
    text_arr = np.reshape(text_arr, (-1, (np.shape(key)[0])))
    # print(text,text_arr)

    out = np.mod(np.dot(key, text_arr.T), 26).astype(int)
    out = out.T
    out = np.reshape(out, (-1, 1))
    out_ls = out.astype(list)

    out_str = ""
    for i, val in enumerate(out_ls):
        out_str = out_str + dic[int(val)]

    return out_str


# testing
'''
out = Hill("short example", [[7, 8], [11, 11]])
print(out)

x = input("key matrix\n")
print(np.array(x))
'''

delete_file_content("Input Files\Hill\hill_cipher_3x3.txt")
for line in read("Input Files\Hill\hill_plain_3x3.txt"):
    out = Hill(line, [[2, 4, 12], [9, 1, 6], [7, 5, 3]])
    print(out)
    write("Input Files\Hill\hill_cipher_3x3.txt", out)


delete_file_content("Input Files\Hill\hill_cipher_2x2.txt")
for line in read("Input Files\Hill\hill_plain_2x2.txt"):
    out = Hill(line, [[5, 17], [8, 3]])
    print(out)
    write("Input Files\Hill\hill_cipher_2x2.txt", out)
