import sys
input = sys.stdin.readline
n = int(input())
s = [0, 1, 0, 0]
for i in range(n):
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]
for i in range(1, 4):
    if s[i] == 1: print(i)