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

    # Plain Text expansion Table (32 bits to 48 bits)
    expansion_table = [32, 1, 2, 3, 4, 5, 4, 5,
                       6, 7, 8, 9, 8, 9, 10, 11,
                       12, 13, 12, 13, 14, 15, 16, 17,
                       16, 17, 18, 19, 20, 21, 20, 21,
                       22, 23, 24, 25, 24, 25, 26, 27,
                       28, 29, 28, 29, 30, 31, 32, 1]

    # Straight Permutation Table
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

    # Final Permutation Table (Compression) (64 bits to 56 bits)
    final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
                  39, 7, 47, 15, 55, 23, 63, 31,
                  38, 6, 46, 14, 54, 22, 62, 30,
                  37, 5, 45, 13, 53, 21, 61, 29,
                  36, 4, 44, 12, 52, 20, 60, 28,
                  35, 3, 43, 11, 51, 19, 59, 27,
                  34, 2, 42, 10, 50, 18, 58, 26,
                  33, 1, 41, 9, 49, 17, 57, 25]

    # First key permutation choice
    first_permutation_choice = [57, 49, 41, 33, 25, 17, 9,
                                1, 58, 50, 42, 34, 26, 18,
                                10, 2, 59, 51, 43, 35, 27,
                                19, 11, 3, 60, 52, 44, 36,
                                63, 55, 47, 39, 31, 23, 15,
                                7, 62, 54, 46, 38, 30, 22,
                                14, 6, 61, 53, 45, 37, 29,
                                21, 13, 5, 28, 20, 12, 4]

    # Number of bit shifts
    shift_table = [1, 1, 2, 2,
                   2, 2, 2, 2,
                   1, 2, 2, 2,
                   2, 2, 2, 1]

    # Second key permutation choice (Compression) (key 56 bits to 48 bits)
    second_permutation_choice = [14, 17, 11, 24, 1, 5,
                                 3, 28, 15, 6, 21, 10,
                                 23, 19, 12, 4, 26, 8,
                                 16, 7, 27, 20, 13, 2,
                                 41, 52, 31, 37, 47, 55,
                                 30, 40, 51, 45, 33, 48,
                                 44, 49, 39, 56, 34, 53,
                                 46, 42, 50, 36, 29, 32]

    initial_perm = np.array(initial_perm)
    initial_perm = np.reshape(initial_perm, (np.shape(initial_perm)[0], 1))

    expansion_table = np.array(expansion_table)
    expansion_table = np.reshape(expansion_table, (np.shape(expansion_table)[0], 1))

    per = np.array(per)
    per = np.reshape(per, (np.shape(per)[0], 1))

    sbox = np.array(sbox)

    final_perm = np.array(final_perm)
    final_perm = np.reshape(final_perm, (np.shape(final_perm)[0], 1))

    first_permutation_choice = np.array(first_permutation_choice)
    first_permutation_choice = np.reshape(first_permutation_choice, (np.shape(first_permutation_choice)[0], 1))

    shift_table = np.array(shift_table)
    shift_table = np.reshape(shift_table, (np.shape(shift_table)[0], 1))

    second_permutation_choice = np.array(second_permutation_choice)
    second_permutation_choice = np.reshape(second_permutation_choice, (np.shape(second_permutation_choice)[0], 1))

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

    # convert binary to decimal
    def bin_to_dec(binary):

        binary1 = binary
        decimal, i, n = 0, 0, 0
        while (binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        return decimal

        # Decimal to binary conversion

    # convert decimal to binary
    def dec_to_bin(num):
        res = bin(num).replace("0b", "")
        if len(res) % 4 != 0:
            div = len(res) / 4
            div = int(div)
            counter = (4 * (div + 1)) - len(res)
            for i in range(0, counter):
                res = '0' + res
        return res

        # permute function

    def permutation_box(txt_arr, perm_arr):
        txt_arr_cpy = np.copy(txt_arr)
        txt_arr_cpy = np.reshape(txt_arr_cpy, (np.shape(txt_arr_cpy)[0] * np.shape(txt_arr_cpy)[1], 1))
        n_txt = np.zeros_like(perm_arr)
        for i in range(len(perm_arr)):
            n_txt[i] = txt_arr_cpy[perm_arr[i] - 1]

        n_txt = np.reshape(n_txt, (np.shape(txt_arr)[0], -1))
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
    def xor_mat(a, b):
        a_cpy = np.copy(a)
        b_cpy = np.copy(b)
        out = np.bitwise_xor(a_cpy, b_cpy)
        return out

    ####################################################################################################################
    # Key Generation
    def k_generation(input_key_hex):
        # convert hex key and plain text to bin
        key_bin = np.chararray((64, 1))
        for i in range(64):
            key_bin[i] = list(hex_to_bin(input_key_hex))[i]
        key_bin = key_bin.decode()

        # first permutation 56 bits to 64 bits
        key_bin = np.reshape(key_bin, (8, 8))
        key_bin = permutation_box(key_bin, first_permutation_choice)

        # split key into two 28 bit parts
        left_k = key_bin[0:4, :]
        right_k = key_bin[4:8, :]

        # 16 round key generation
        round_keys = []
        for i in range(16):
            # shift n bits to left according to shift table
            left_k = shift(left_k, shift_table[i])
            right_k = shift(right_k, shift_table[i])

            # combine left and right parts
            combined_k = np.concatenate((left_k, right_k))

            # second permutation choice , compress key 56 bits to 48 bits
            round_key = permutation_box(combined_k, second_permutation_choice)

            round_keys.append(round_key)

        return round_keys

    ####################################################################################################################
    # Encryption Algorithm (also the decryption algorithm if the round keys are inverted)
    def encrypt(round_keys, text):

        # convert hex key and plain text to bin
        txt_bin = np.chararray((64, 1))
        for i in range(64):
            txt_bin[i] = list(hex_to_bin(text))[i]
        txt_bin = np.reshape(txt_bin, (8, 8)).decode()

        # initial text permutation
        txt_bin = permutation_box(txt_bin, initial_perm)

        # split text into two 32 bit parts
        left_txt = txt_bin[0:4, :]
        right_txt = txt_bin[4:8, :]

        # 16 round encryption
        for i in range(16):
            # right text expanded
            right_txt_exp = permutation_box(right_txt, expansion_table)
            right_txt_exp = np.reshape(right_txt_exp, (8, 6))

            # xor round key with right text expanded
            right_xor_key_result = xor_mat(round_keys[i], right_txt_exp)

            # s-box
            sbox_str = ""
            right_xor_key_result_cpy = np.copy(right_xor_key_result)
            right_xor_key_result_cpy = np.reshape(right_xor_key_result_cpy, (
                np.shape(right_xor_key_result_cpy)[0] * np.shape(right_xor_key_result_cpy)[1], 1))
            for j in range(8):
                row = bin_to_dec(
                    int(str(right_xor_key_result_cpy[j * 6][0]) + str(right_xor_key_result_cpy[j * 6 + 5][0])))
                col = bin_to_dec(
                    int(str(right_xor_key_result_cpy[j * 6 + 1][0]) + str(right_xor_key_result_cpy[j * 6 + 2][0]) +
                        str(right_xor_key_result_cpy[j * 6 + 3][0]) + str(right_xor_key_result_cpy[j * 6 + 4][0])))
                val = sbox[j][int(row)][int(col)]
                sbox_str = sbox_str + dec_to_bin(val)
            right_sbox_ls = list(sbox_str)
            right_sbox_res_mat = np.chararray((len(right_sbox_ls), 1))

            for l in range(len(right_sbox_ls)):
                right_sbox_res_mat[l] = right_sbox_ls[l]
            right_sbox_res_mat = right_sbox_res_mat.decode().astype(int)
            right_sbox_res_mat = np.reshape(right_sbox_res_mat, (8, 4))

            # permutation
            right_perm = permutation_box(right_sbox_res_mat, per)
            right_perm = right_perm.flatten()

            # xor left txt and right perm
            left_txt = left_txt.flatten()
            left_txt = xor_mat(left_txt, right_perm)
            left_txt = np.reshape(left_txt, np.shape(right_txt))

            # swap left and right
            if (i != 15):
                left_txt, right_txt = right_txt, left_txt

        # combine
        left_flat = left_txt.flatten()
        right_flat = right_txt.flatten()
        combine = np.concatenate((left_flat, right_flat), axis=0)
        combine = np.reshape(combine, (8, 8))

        # final permutation
        cipher_txt = permutation_box(combine, final_perm)
        c = cipher_txt.flatten()
        s = str(c).replace(" ", "").replace("\n", "").replace("[", "").replace("]", "")
        cipher_txt_hex = bin_to_hex(s)

        return cipher_txt, cipher_txt_hex

    ####################################################################################################################
    # Round keys generation
    round_key = k_generation(key)
    round_key_inv = round_key[::-1]

    if e_or_d == "e":
        cypher_bin, cypher_hex = encrypt(round_key, text)
        return cypher_hex
    elif e_or_d == "d":
        plain_bin, plain_hex = encrypt(round_key_inv, text)
        return plain_hex


########################################################################################################################
# testing
'''
inputt = "CE20031574D2C98F"
for i in range(10):
    inputt = DES("0123456789ABCDEF", inputt, "d")
    print(inputt)
'''