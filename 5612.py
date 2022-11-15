# 5612번: 터널의 입구와 출구

n = int(input())
m = int(input())
result = m
temp = m
for _ in range(n):
    a, b = map(int, input().split())
    temp = temp + a - b
    if temp < 0:
        result = 0
        break
    if result < temp:
        result = temp
print(result)