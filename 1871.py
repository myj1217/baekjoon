# 1871번: 좋은 자동차 번호판

for _ in range(int(input())):
    L, D = input().split('-')
    n = int(D)
    s = 0
    for i in range(3):
        s += (ord(L[i]) - 65) * 26 ** (2 - i)
    print("nice" if abs(s-n) <= 100 else "not nice")