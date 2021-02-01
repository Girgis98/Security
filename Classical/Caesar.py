from read_and_save import *


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


# Testing
'''
lista = []
ok = True
for i in range (-1000,1000):
    out = Caesar("abcdefghijklmnopqrstuvwxyz", i)

   # print(out)
    out = Caesar(out,i,"d")
    lista.append(out)
    print(out)
for i in range(len(lista)-1):
    if lista[i] != lista[i+1]:
        ok = False
if ok :
    print("OK")
else:
    print("NO")
'''

delete_file_content("D:\Desktop\To Do\security\Projects\Classical\Input Files\Caesar\caesar_cipher_3.txt")
for line in read("D:\Desktop\To Do\security\Projects\Classical\Input Files\Caesar\caesar_plain.txt"):
    out = Caesar(line, 3)
    print(out)
    write("D:\Desktop\To Do\security\Projects\Classical\Input Files\Caesar\caesar_cipher_3.txt", out)

delete_file_content("D:\Desktop\To Do\security\Projects\Classical\Input Files\Caesar\caesar_cipher_6.txt")
for line in read("D:\Desktop\To Do\security\Projects\Classical\Input Files\Caesar\caesar_plain.txt"):
    out = Caesar(line, 6)
    print(out)
    write("D:\Desktop\To Do\security\Projects\Classical\Input Files\Caesar\caesar_cipher_6.txt", out)

delete_file_content("D:\Desktop\To Do\security\Projects\Classical\Input Files\Caesar\caesar_cipher_12.txt")
for line in read("D:\Desktop\To Do\security\Projects\Classical\Input Files\Caesar\caesar_plain.txt"):
    out = Caesar(line, 12)
    print(out)
    write("D:\Desktop\To Do\security\Projects\Classical\Input Files\Caesar\caesar_cipher_12.txt", out)
