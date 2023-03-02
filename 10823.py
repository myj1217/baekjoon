# 10823번: 더하기 2

s = ''
while 1:
    try:
        s += input()
    except:
        break
print(sum(map(int, s.split(','))))