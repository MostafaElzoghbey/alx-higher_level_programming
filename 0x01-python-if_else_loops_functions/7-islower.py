#!/usr/bin/python3
def islower(c):
    # Returns True if the given character is lowercase, False otherwise.

    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
