# 3047번: ABC

num_li = sorted(map(int, input().split())) 
for c in input(): 
    print(num_li[ord(c) - ord('A')], end = ' ')