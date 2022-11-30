# 6378번: 디지털 루트

while True: 
    n = int(input()) 
    if n: 
        while(n > 9): 
            n = sum(map(int, list(str(n)))) 
        print(n) 
    else: 
        break