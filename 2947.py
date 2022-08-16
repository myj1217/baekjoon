# 2947번: 나무 조각

li = list(map(int, input().split()))
for i in range(5):
    for j in range(4):
        if li[j] > li[j + 1]:
            t = li[j]
            li[j] = li[j + 1]
            li[j + 1] = t
            print(*li)