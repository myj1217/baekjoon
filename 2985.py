# 2985번: 세 수

a, b, c = map(int, input().split())
if a + b == c:
    print(f"{a}+{b}={c}")
elif a - b == c:
    print(f"{a}-{b}={c}")
elif a * b == c:
    print(f"{a}*{b}={c}")
elif a // b == c:
    print(f"{a}/{b}={c}")
elif a == b + c:
    print(f"{a}={b}+{c}")
elif a == b - c:
    print(f"{a}={b}-{c}")
elif a == b * c:
    print(f"{a}={b}*{c}")
elif a == b // c:
    print(f"{a}={b}/{c}")