# 2965번: 캥거루 세마리

A, B, C = map(int, input().split()) 
print(max(B - A - 1, C - B - 1))