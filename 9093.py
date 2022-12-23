# 9093번: 단어 뒤집기

for _ in range(int(input())):
    li = input().split()
    for s in li:
        print(s[::-1], end=' ')
    print()