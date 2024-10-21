#!/usr/bin/python3
print("{}".format(
    ''.join(chr((i - 65) % 26 + (65 if i % 2 else 97)) for i in range(90, 64, -1))
), end="")
