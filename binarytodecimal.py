def binarytodecimal(num):
    b = list(str(num)).reverse()
    dec = 0
    for i in range(0,len(b)):
        num = int(b[i])*(2**i)
        dec += num
    return dec
