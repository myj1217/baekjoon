# 3058번: 짝수를 찾아라

for _ in range(int(input())):
    li = list(map(int, input().split()))
    even_li = []
    for n in li:
        if n % 2 == 0:
            even_li.append(n)
    print(sum(even_li), min(even_li))