# 4101번: 크냐?

while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print("Yes" if a > b else "No")