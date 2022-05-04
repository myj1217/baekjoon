N = int(input()) 
li = [False] * 100 
p = list(map(int, input().split())) 
cnt = 0 

for n in p: 
    if li[n-1] == False: 
        li[n-1] = True 
    else: 
        cnt += 1 
         
print(cnt)