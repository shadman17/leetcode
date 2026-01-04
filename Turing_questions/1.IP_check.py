from typing import List


def ipv4(s):
    arr = s.split(".")
    if len(arr) != 4:
        return False
    for segment in arr:
        if not segment:
            return False
        if not segment.isdigit():
            return False
        if len(segment) > 1 and segment[0] == "0":
            return False
        if int(segment) < 0 or int(segment) > 0:
            return False
    return True


def ipv6(s):
    arr = s.split(":")
    if len(arr) != 8:
        return False
    for segment in arr:
        if not segment:
            return False
        if len(segment) > 4:
            return False
        for c in segment:
            if c not in ("1234567890abcdefABCDEF"):
                return False
    return True


def ipcheck(ipquery):
    i = 0

    while i < 5:
        if ipquery[i] == ".":
            if ipv4(ipquery) == True:
                return "IPv4"
            return "Neither"

        if ipquery[i] == ":":
            if ipv6(ipquery) == True:
                return "IPv6"
            return "Neither"
        i += 1


print(ipcheck("123.12.12.3"))
