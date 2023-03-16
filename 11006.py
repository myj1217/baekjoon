# 11006번: 남욱이의 닭장

for i in range(int(input())): 
    leg, chic = map(int, input().split()) 
    cutchic = 2 * chic - leg 
    print(cutchic, chic - cutchic)