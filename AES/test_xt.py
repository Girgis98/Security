
#multi_by_two = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)
xtime = lambda a: (a << 1) if (not(a & 0x80)) else (((a << 1) ^ 0x1B) & 0xFF) #if (a & 0x80) else 0
b = xtime(0x01)
print(b)
