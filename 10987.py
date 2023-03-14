# 10987번: 모음의 개수

answer = 0
for c in input():
    if c in ['a', 'e', 'i', 'o', 'u']:
        answer += 1
print(answer)