# 10174번: 팰린드롬

for _ in range(int(input())):
    s = input().lower()
    print("Yes" if s == s[::-1] else "No")