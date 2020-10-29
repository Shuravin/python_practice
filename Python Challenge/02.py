my_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

mychar = "aba"

url = "http://www.pythonchallenge.com/pc/def/map.html"


def decrypting(string):
    result = ''
    for x in string:
        ch = str(x)
        if ch == "a":
            result += "c"
        elif ch == "b":
            result += "d"
        elif ch == "c":
            result += "e"
        elif ch == "d":
            result += "f"
        elif ch == "e":
            result += "g"
        elif ch == "f":
            result += "h"
        elif ch == "g":
            result += "i"
        elif ch == "h":
            result += "j"
        elif ch == "i":
            result += "k"
        elif ch == "j":
            result += "l"
        elif ch == "k":
            result += "m"
        elif ch == "l":
            result += "n"
        elif ch == "m":
            result += "o"
        elif ch == "n":
            result += "p"
        elif ch == "o":
            result += "q"
        elif ch == "p":
            result += "r"
        elif ch == "q":
            result += "s"
        elif ch == "r":
            result += "t"
        elif ch == "s":
            result += "u"
        elif ch == "t":
            result += "v"
        elif ch == "u":
            result += "w"
        elif ch == "v":
            result += "z"
        elif ch == "w":
            result += "y"
        elif ch == "x":
            result += "z"
        elif ch == "y":
            result += "a"
        elif ch == "z":
            result += "b"
        else:
            result += ch
    print(result)


decrypting(url)
