#!/usr/bin/python3
print("{}".format("".join(chr((i - 97 + 65 * (i % 2)) % 26 + 97 - 32 * (i % 2)) for i in range(122, 96, -1))), end="")
