def octaltodecimal(num):
    octal = list(str(num))
    octal.reverse()
    dec = 0
    for i in range(0,len(octal)):
        num = int(octal[i])*(8**i)
        dec += num
    return dec
