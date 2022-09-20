# 4458번: 첫 글자를 대문자로

for _ in range(int(input())):
    s = list(input())
    s[0] = s[0].upper()
    print(''.join(s))