import numpy as np
from math import *


def main(plain_text, caesar_key, hill_key, play_fair_key, vigenere_key, vigenere_mode, vernam_key):
    def Caesar(text, key, e_or_d = 'e'):
        text = text.lower()
        text = text.replace(" ", "").replace("\n", "")
        out = ""
        dic = {
            0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l",
            12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x",
            24: "y", 25: "z"
        }
        dic2 = {
            "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
            "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
            "y": 24, "z": 25}

        if e_or_d == "e":
            for itr in text:
                itr = dic[((dic2[itr] + key) % 26)]
                out = out + itr
            return out

        elif e_or_d == "d":
            for i in text:
                i = dic[((dic2[i] - key) % 26)]
                out = out + i
            return out

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

    def Vigenere(text, key, mode):  # mode : true auto , false repeating

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

        # complete key
        for i in range(len(text) - len(key)):
            if mode:  # auto
                key = key + text[i]
            elif not mode:  # repeat
                key = key + key[i]

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

    caesar_cipher_text = Caesar(plain_text, caesar_key)
    hill_cipher_text = Hill(plain_text, hill_key)
    play_fair_cipher_text = play_fair(plain_text, play_fair_key)
    vigenere_cipher_text = Vigenere(plain_text, vigenere_key, vigenere_mode)
    vernam_cipher_text = Vernam(plain_text, vernam_key)
    return caesar_cipher_text, hill_cipher_text, play_fair_cipher_text, vigenere_cipher_text, vernam_cipher_text



h_row = []
while (True):
    PL_text = input("Please Enter Plain Text : ")
    c_key = int(input("Please Enter Caesar key : "))
    h_size = int(input("Please Enter Hill key size : "))
    h_key_str = input("Please Enter Hill key : ")
    p_key = input("Please Enter PlayFair key : ")
    vig_key = input("Please Enter Vigenere key : ")
    vig_mode = bool(input("Please Enter Vigenere mode : "))
    ver_key = input("Please Enter Vernam key : ")

    # PL_text = "Hello"
    # c_key = int("2")
    # h_size = int("2")
    # h_key_str = ("5 17,8 3")
    # p_key = ("rats")
    # vig_key = ("pie")
    # vig_mode = bool("True")
    # ver_key = ("SPARTANS")

    # input hill cipher key
    h_key = []
    h_temp = []
    for i in range(h_size):
        for j in range(h_size):
            h_temp.append(1)
        h_key.append(h_temp.copy())
        h_temp.clear()

    h_row_list = h_key_str.split(",")
    for i in range(len(h_row_list)):
        h_col_list = h_row_list[i].split()
        for j in range(len(h_col_list)):
            h_key[i][j] = int(h_col_list[j])


    c_out, h_out, p_out, vig_out, ver_out = main(PL_text, c_key, h_key, p_key, vig_key, vig_mode, ver_key)
    print("Caesar Cipher text : ", c_out)
    print("Caesar Hill text : ", h_out)
    print("Caesar PlayFair text : ", p_out)
    print("Caesar Vigenere text : ", vig_out)
    print("Caesar Vernam text : ", ver_out)
