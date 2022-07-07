# 2506번: 점수계산

N = int(input())
li = list(map(int, input().split()))
res = 0
cnt = 0
for n in li:
    if n == 1:
        cnt += 1
    else:
        res += cnt * (cnt + 1) // 2
        cnt = 0
res += cnt * (cnt + 1) // 2
print(res)