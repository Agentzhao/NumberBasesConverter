def decimaltoocta(dec):
    num = int(dec)
    octal = []
    while (num > 0):
        rem = num % 8
        octal.append(str(rem))
        num = num // 8
    octal.reverse()
    return(''.join(octal))
