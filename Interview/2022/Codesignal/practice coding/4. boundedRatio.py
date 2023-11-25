def boundedRatio(a, l, r):
    n = len(a)
    b = [False] * n
    for i, num in enumerate(a):
        for x in range(l, r+ 1):
            print(i, num, x)
            if num == x * (i + 1):
                b[i] = True
                break
    return b

a = [8, 5, 6, 16, 5]
l, r = 1, 3
print(boundedRatio(a, l, r))
