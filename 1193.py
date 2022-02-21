n = int(input()) # 입력
num = 0 # 1, 3, 6, 10, 15... 순으로 증가하는 라인별 총 수
cnt = 1 # num값을 2, 3, 4... 씩 순차적으로 더해주기 위한 변수
 
while n > num : # 입력받은 값이 num값보다 큰 동안
    num += cnt # num = num + cnt
    cnt += 1 # cnt는 1씩 증가
 
b = n - (num - (cnt - 1)) # b = 라인에서 몇 번째
 
# 짝수와 홀수로 나누어서 지그재그 구현
if cnt % 2 == 0: 
    print(str(cnt-b)+'/'+str(b))
else:
    print(str(b)+'/'+str(cnt-b))