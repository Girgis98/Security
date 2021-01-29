import numpy as np
from math import *


def DES(text, key, e_or_d):



    def convert_str_to_bin(str):
        str_cpy = str
        byte_array = bytearray(str_cpy, "utf8")
        byte_ls = []
        all_bytes = ""
        for byte in byte_array:
            binary = bin(byte).replace("0b", "")
            byte_ls.append(binary)
        all_bytes = ''.join(byte_ls)
        return all_bytes

    a = convert_str_to_bin("abc")
    print(a)


# testing
DES(1, 1, 1)
