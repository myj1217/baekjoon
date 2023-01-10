# 9610번: 사분면

li = [0] * 5
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        li[4] += 1
    elif x > 0 and y > 0:
        li[0] += 1
    elif x < 0 and y > 0:
        li[1] += 1
    elif x < 0 and y < 0:
        li[2] += 1
    else:
        li[3] += 1
for i in range(4):
    print(f"Q{i + 1}: {li[i]}")
print(f"AXIS: {li[4]}")