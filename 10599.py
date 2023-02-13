# 10599번: 페르시아의 왕들

while 1:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0:
        break
    print(c - b, d - a)