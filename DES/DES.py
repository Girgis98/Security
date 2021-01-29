import numpy as np
from math import *
from bitarray import *


def DES(key, text, e_or_d):
    ####################################################################################################################
    # Tables

    # Initial Permutation Table
    initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                    60, 52, 44, 36, 28, 20, 12, 4,
                    62, 54, 46, 38, 30, 22, 14, 6,
                    64, 56, 48, 40, 32, 24, 16, 8,
                    57, 49, 41, 33, 25, 17, 9, 1,
                    59, 51, 43, 35, 27, 19, 11, 3,
                    61, 53, 45, 37, 29, 21, 13, 5,
                    63, 55, 47, 39, 31, 23, 15, 7]

    # Expansion D-box Table
    exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
             6, 7, 8, 9, 8, 9, 10, 11,
             12, 13, 12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21, 20, 21,
             22, 23, 24, 25, 24, 25, 26, 27,
             28, 29, 28, 29, 30, 31, 32, 1]

    # Straight Permutaion Table
    per = [16, 7, 20, 21,
           29, 12, 28, 17,
           1, 15, 23, 26,
           5, 18, 31, 10,
           2, 8, 24, 14,
           32, 27, 3, 9,
           19, 13, 30, 6,
           22, 11, 4, 25]

    # S-box Table
    sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    # Final Permutaion Table
    final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                  39, 7, 47, 15, 55, 23, 63, 31,
                  38, 6, 46, 14, 54, 22, 62, 30,
                  37, 5, 45, 13, 53, 21, 61, 29,
                  36, 4, 44, 12, 52, 20, 60, 28,
                  35, 3, 43, 11, 51, 19, 59, 27,
                  34, 2, 42, 10, 50, 18, 58, 26,
                  33, 1, 41, 9, 49, 17, 57, 25]

    initial_perm = np.array(initial_perm)
    initial_perm = np.reshape(initial_perm, (np.shape(initial_perm)[0], 1))

    exp_d = np.array(exp_d)
    exp_d = np.reshape(exp_d, (np.shape(exp_d)[0], 1))

    per = np.array(per)
    per = np.reshape(per, (np.shape(per)[0], 1))

    sbox = np.array(sbox)

    final_perm = np.array(final_perm)
    final_perm = np.reshape(final_perm, (np.shape(final_perm)[0], 1))

    ####################################################################################################################

    # Functions

    # convert hex to binary
    def hex_to_bin(hex_str):
        dic1 = {'0': "0000",
                '1': "0001",
                '2': "0010",
                '3': "0011",
                '4': "0100",
                '5': "0101",
                '6': "0110",
                '7': "0111",
                '8': "1000",
                '9': "1001",
                'A': "1010",
                'B': "1011",
                'C': "1100",
                'D': "1101",
                'E': "1110",
                'F': "1111"}
        bin_str = ""
        for i in range(len(hex_str)):
            bin_str = bin_str + dic1[hex_str[i]]
        return bin_str

    # convert binary to hex
    def bin_to_hex(bin_str):
        dic2 = {"0000": '0',
                "0001": '1',
                "0010": '2',
                "0011": '3',
                "0100": '4',
                "0101": '5',
                "0110": '6',
                "0111": '7',
                "1000": '8',
                "1001": '9',
                "1010": 'A',
                "1011": 'B',
                "1100": 'C',
                "1101": 'D',
                "1110": 'E',
                "1111": 'F'}
        hex_str = ""
        for i in range(0, len(bin_str), 4):
            chr = ""
            for j in range(4):
                chr = chr + bin_str[j + i]
            hex_str = hex_str + dic2[chr]
        return hex_str

    # permute function
    def permutation_box(txt_arr, perm_arr):
        txt_arr_cpy = np.copy(txt_arr)
        txt_arr_cpy = np.reshape(txt_arr_cpy, (np.shape(txt_arr_cpy)[0] * np.shape(txt_arr_cpy)[1], 1))
        n_txt = np.zeros_like(txt_arr_cpy)
        for i, val in enumerate(txt_arr_cpy):
            n_txt[i] = txt_arr_cpy[perm_arr[i] - 1]

        n_txt = np.reshape(n_txt, np.shape(txt_arr))
        return n_txt

    # shift left function
    def shift(arr, number_of_shifts):
        arr_cpy = np.copy(arr)
        arr_cpy = np.reshape(arr_cpy, ((np.shape(arr_cpy)[0] * np.shape(arr_cpy)[1], 1)))
        out = np.zeros_like(arr_cpy)
        for i, val in enumerate(arr_cpy):
            out[i] = arr_cpy[(i + number_of_shifts) % len(arr_cpy)]
        out = np.reshape(out, np.shape(arr))
        return out

    # xor two equal length strings
    def xor_str(a, b):
        out = ""
        for i in range(len(a)):
            out = out + str(int(a[i]) ^ int(b[i]))

    ####################################################################################################################

    # Encryption Algorithm

    # convert hex key and plain text to bin
    txt_bin = np.chararray((64, 1))
    key_bin = np.chararray((64, 1))
    for i in range(64):
        txt_bin[i] = list(hex_to_bin(text))[i]
        key_bin[i] = list(hex_to_bin(key))[i]

    txt_bin = np.reshape(txt_bin, (8, 8)).decode()
    key_bin = np.reshape(key_bin, (8, 8)).decode()

    # initial text permuation
    txt_bin = permutation_box(txt_bin, initial_perm)

    # remove 8th element from each column in key to get 56 bits
    key_bin = key_bin[:, 0:7]



########################################################################################################################
# testing
DES("0123456789ABCDEF", "0123456789ABCDEF", "e")
