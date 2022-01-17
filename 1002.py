import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    
    # 두 원의 중심 사이의 거리
    dis = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    # 두 원의 중심이 같을 경우
    if dis == 0:
        # 두 원의 크기가 같아 겹치는 경우
        if r1 == r2: 
            print(-1)
        # 한 원이 다른 원 안에 들어가 있는 경우
        else:                     
            print(0)
    # 두 원의 중심이 다를 경우
    else:            
        if r1+r2 == dis or abs(r2-r1) == dis:
            print(1)
        elif ((abs(r1-r2) < dis) and (dis < r1+r2)):
            print(2)
        else:
            print(0)