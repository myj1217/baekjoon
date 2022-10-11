# 5043번: 정말 좋은 압축

N, b = map(int, input().split())
print('yes' if N <= 2 ** (b + 1) - 1 else 'no')