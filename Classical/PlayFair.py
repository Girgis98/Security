import numpy as np
from math import *


def play_fair(text, e_or_d, key):
    dic2 = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "k": 9, "l": 10,
        "m": 11, "n": 12, "o": 13, "p": 14, "q": 15, "r": 16, "s": 17, "t": 18, "u": 19, "v": 20, "w": 21, "x": 22,
        "y": 23, "z": 24}
    dic_cpy = dic2.copy()

    # lowercase
    text = text.lower()
    key = key.lower()

    # remove whitespaces
    text = text.replace(" ", "")
    key = key.replace(" ", "")

    # replace j with i
    text = text.replace("j", "i")
    key = key.replace("j", "i")

    # add x to two identical letters
    key_len = len(key)
    itr = 0
    while itr < (key_len - 1):
        if (key[itr] == key[itr + 1]) and itr % 2 == 0:
            key_ls = list(key)
            key_ls.insert(itr + 1, 'x')
            key_ls = ''.join(key_ls)
            key = key_ls
            key_len += 1
        itr += 1

    txt_len = len(text)
    itrx = 0
    while itrx < (txt_len - 1):
        if (text[itrx] == text[itrx + 1]) and itrx % 2 == 0:
            text_ls = list(text)
            text_ls.insert(itrx + 1, 'x')
            text_ls = ''.join(text_ls)
            text = text_ls
            txt_len += 1
        itrx += 1

    # make text even
    if len(text) % 2 == 1:
        text = text + 'x'

    # 5x5 matrix creation
    mat = np.chararray((5, 5))
    key_itr = 0
    last_i = 0
    last_j = 0
    for i in range(ceil(len(key) / 5)):
        for j in range(5):
            if key[key_itr] in dic_cpy.keys():
                mat[i][j] = key[key_itr]
                dic_cpy.pop(key[key_itr])
            key_itr += 1
            last_j = j
            last_i = i
            if key_itr == len(key):
                break

    dic_itr = 0
    for i in range(ceil(len(dic_cpy) / 5)):
        for j in range(5):
            if list(dic_cpy.keys())[dic_itr] in dic_cpy.keys():
                mat[i][j] = list(dic_cpy.keys())[dic_itr]
                dic_cpy.pop(list(dic_cpy.keys())[dic_itr])
            dic_itr += 1
            if dic_itr == len(dic_cpy):
                break


play_fair("my name is Gargosaaa mamdouhe", "e", "eeeeeeeee")
