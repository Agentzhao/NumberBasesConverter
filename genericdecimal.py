bases = {'1':'1',
         '2':'2',
         '3':'3',
         '4':'4',
         '5':'5',
         '6':'6',
         '7':'7',
         '8':'8',
         '9':'9',
         'A':'10',
         'B':'11',
         'C':'12',
         'D':'13',
         'E':'14',
         'F':'15'}

def genericdecimal():
    num = str(input("Enter a number: "))
    base = int(input("Enter the base it is in: "))
    listnum = list(num)
    listnum.reverse()
    dec = 0
    for i in range(0,len(listnum)):
        num = int(bases[listnum[i]])*(base**i)
        dec += num
    return dec
