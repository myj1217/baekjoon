# 4564번: 숫자 카드놀이

while 1:
    n = input()
    if n == '0':
        break
    while len(n) > 1:
        res = 1
        print(n, end=' ')
        for c in n:
            res *= int(c)
        n = str(res)
    print(n)