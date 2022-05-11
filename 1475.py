# 1475번 방 번호

n = input() 
list = [0] * 9
for i in n: 
    i = int(i) 
    if i == 9: 
        i = 6 
    list[i] += 1 
list[6] = (list[6] + 1) // 2 
print(max(list))