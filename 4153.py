# 4153번: 직각삼각형

while True:
    li = sorted(list(map(int, input().split())))
    if sum(li) == 0:
        break
    if li[0] ** 2 + li[1] ** 2 == li[2] ** 2:
        print('right')
    else:
        print('wrong')