def binarytodecimal(num):
    b = list(str(num)).reverse()
    dec = 0
    base = 2
    for i in range(0,len(b)):
        num = int(b[i])*(base**i)
        dec += num
    return dec
