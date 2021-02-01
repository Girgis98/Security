import numpy as np
from math import *
from read_and_save import *


def play_fair(text, key):
    dic2 = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "k": 9, "l": 10,
        "m": 11, "n": 12, "o": 13, "p": 14, "q": 15, "r": 16, "s": 17, "t": 18, "u": 19, "v": 20, "w": 21, "x": 22,
        "y": 23, "z": 24}
    dic_cpy = dic2.copy()

    # lowercase
    text = text.lower()
    key = key.lower()

    # remove whitespaces
    text = text.replace(" ", "").replace("\n", "")
    key = key.replace(" ", "").replace("\n", "")

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
    mat = np.chararray((25, 1))

    mat_itr = 0
    for i in range((len(key))):
        if key[i] in dic_cpy.keys():
            mat[mat_itr] = key[i]
            dic_cpy.pop(key[i])
            mat_itr += 1

    for i, ele in enumerate(dic_cpy):
        if list(dic_cpy.keys())[i] in dic_cpy.keys():
            mat[mat_itr] = list(dic_cpy.keys())[i]
            mat_itr += 1

    mat = mat.decode('utf-8')
    mat = np.reshape(mat, (5, 5))

    # print(mat)

    def get_position(char, mat_c):
        mat_cpy = np.copy(mat_c)
        mat_cpy = np.reshape(mat_cpy, (25, 1))

        for i, val in enumerate(mat_cpy):
            if char == val:
                pos = i
                break
        pos_x = pos % 5
        pos_y = floor(pos / 5)
        return pos_x, pos_y

    # test get position
    '''
    for i, val in enumerate(np.reshape(mat, (25, 1))):
        x, y = get_position(val, mat)
        print(x, y)
    '''
    out = ""
    for i in range(0, len(text) - 1, 2):
        pos_x_i, pos_y_i = get_position(text[i], mat)
        pos_x_i_p, pos_y_i_p = get_position(text[i + 1], mat)

        if pos_y_i == pos_y_i_p:
            out = out + mat[pos_y_i][(pos_x_i + 1) % 5]
            out = out + mat[pos_y_i_p][(pos_x_i_p + 1) % 5]
        elif pos_x_i == pos_x_i_p:
            out = out + mat[(pos_y_i + 1) % 5][pos_x_i]
            out = out + mat[(pos_y_i_p + 1) % 5][pos_x_i_p]
        else:
            out = out + mat[pos_y_i][pos_x_i_p]
            out = out + mat[pos_y_i_p][pos_x_i]
    return out


# testing
'''
o = play_fair("hello world", "charles")
print(o)
'''

delete_file_content("D:\Desktop\To Do\security\Projects\Classical\Input Files\PlayFair\playfair_cipher_rats.txt")
for line in read("D:\Desktop\To Do\security\Projects\Classical\Input Files\PlayFair\playfair_plain.txt"):
    out = play_fair(line, "rats")
    print(out)
    write("D:\Desktop\To Do\security\Projects\Classical\Input Files\PlayFair\playfair_cipher_rats.txt", out)

delete_file_content("D:\Desktop\To Do\security\Projects\Classical\Input Files\PlayFair\playfair_cipher_archangel.txt")
for line in read("D:\Desktop\To Do\security\Projects\Classical\Input Files\PlayFair\playfair_plain.txt"):
    out = play_fair(line, "archangel")
    print(out)
    write("D:\Desktop\To Do\security\Projects\Classical\Input Files\PlayFair\playfair_cipher_archangel.txt", out)
