while 1:
    N = input()
    if N == '0':
        break
    result = len(N)+1
    for n in N:
        if n == '0':
            result += 4 
        elif n == '1':
            result += 2
        else:
            result += 3
    print(result)