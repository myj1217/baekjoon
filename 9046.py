# 9046번: 복호화

for _ in range(int(input())):
    s = input()
    li = [0] * 26
    for c in s:
        if c.isalpha():
            li[ord(c) - ord('a')] += 1
    t = max(li)
    print(chr(ord('a') + li.index(t)) if li.count(t) < 2 else '?')