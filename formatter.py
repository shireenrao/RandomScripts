import math

def format(t):
    secs = 0
    mills = 0
    mins = 0

    mills = t % 10
    secs_total = int(t / 10)

    mins = int(secs_total / 60)
    secs = int(secs_total % 60)
    
    sec_str = ''
    if secs < 9:
        sec_str = '0' + str(secs)
    else:
        sec_str = str(secs)

    print str(mins) + ':' + sec_str + '.' + str(mills) 

format(0)
    
