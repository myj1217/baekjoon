# 10474번: 분수좋아해?

while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(f"{a // b} {a % b} / {b}")