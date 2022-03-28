A, B, N = map(int, input().split())
i = 0
while i < N:
    n = (A%B * 10) // B
    A = (A%B * 10) % B
    i += 1
print(n)