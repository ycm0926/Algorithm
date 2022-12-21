def solution(s, n):
    res = ""
    for i in s:
        if i.isupper():
            res += chr(ord('A') + ((ord(i) + n) - 65) % 26)
        elif i.islower():
            res += chr(ord('a') + ((ord(i) + n) - 97) % 26)
        else:
            res += " "
    return res 