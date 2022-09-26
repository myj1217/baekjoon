# 4504번: 배수 찾기

n = int(input()) 
while 1: 
    t = int(input()) 
    if t == 0: 
        break 
    if t % n != 0: 
        print('{0} is NOT a multiple of {1}.'.format(t, n)) 
    else: 
        print('{0} is a multiple of {1}.'.format(t, n))