# 10093번: 숫자

a, b = map(int,input().split())
m = min(a, b)
n = max(a, b)
if(a == b):
    print(0)
else:
    print(n - m - 1)
    for i in range(m + 1, n):
        print(i, end=' ')