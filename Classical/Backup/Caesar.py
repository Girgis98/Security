def Caesar(text, E_or_D, key):
    text = text.lower()
    text = text.replace(" ", "")
    out = ""
    if E_or_D == "E":
        for i in text:
            if ((ord(i) + key)) > 122:
                i = chr(((ord(i) + key) % 122) + 97)
            elif ((ord(i) + key)) <= 122:
                i = chr(((ord(i) + key) % 122))
            out = out + i
        return out

    elif E_or_D == "D":
        for i in text:
            if ((ord(i) - key)) < 97:
                i = chr(((ord(i) - key) % 122) + 25)
            elif ((ord(i) - key)) >= 97:
                i = chr(((ord(i) - key) % 122))
            out = out + i
        return out




out = Caesar("abcdefghijklmnopqrstuvwxyz","E",3)

print(out)
out = Caesar(out,"D",3)

print(out)


