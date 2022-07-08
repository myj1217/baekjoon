# 2566번: 최댓값

max_n = 0
max_i = 0
max_j = 0
for i in range(1, 10):
    li = list(map(int, input().split()))
    n = max(li)
    if max_n < n:
        max_n = n
        max_i = i
        max_j = li.index(max(li)) + 1
print(max_n)
print(max_i, max_j)