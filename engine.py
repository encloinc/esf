def decode(x):
    i = 0
    i2 = ''
    i3 = 0
    tmp = []
    ret = []
    chars = [' ', '!', '"', "°", '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '/', ']', '^',
             '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '£']
    if len(x) % 2 == 0:
        tmp = []
        i = 0
        while len(x) != i3:
            i2 = x[i] + x[i + 1]
            if i2 == '00':
                ret.append(''.join(tmp))
                tmp = []
            else:
                tmp.append(chars[int(i2) - 1])
            i += 2
            i3 += 2
    return ret


def encode(x):
    i = 0
    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0
    chars = [' ', '!', '"', "°", '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '/', ']', '^',
             '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '£']
    tmp = []
    i = 0
    while len(x) != i4:
        i2 = 0
        i5 = 0
        while len(x[i]) != i5:
            i3 = chars.index(x[i][i2]) + 1
            if i3 == 0:
                tmp.append('9')
                tmp.append('6')
            elif i3 > 10:
                tmp.append(str(i3)[0])
                tmp.append(str(i3)[1])
            else:
                tmp.append('0')
                tmp.append(str(i3))
            i2 += 1
            i5 += 1
        tmp.append("0")
        tmp.append("0")
        i += 1
        i4 += 1
    return (''.join(tmp))
