# 9469번: 폰 노이만

for _ in range(int(input())):
    N, D, A, B, F = map(float, input().split())
    T = D / (A + B) * F
    print("%d %.6f" % (N, T))