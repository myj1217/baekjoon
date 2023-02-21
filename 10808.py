# 10808번: 알파벳 개수

cnt = [0] * 26
for c in input():
      cnt[ord(c) - ord('a')] += 1
print(*cnt)