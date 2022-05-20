N = int(input())
cnt = 0
t = 1
while N:
    if N < t:
        t = 1
    N -= t
    t += 1
    cnt += 1
print(cnt)