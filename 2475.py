# 2475번: 검증수

res = 0
for n in list(map(int, input().split())):
    res += n ** 2
print(res % 10)