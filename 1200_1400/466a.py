n, m, a, b = map(int, input().split())

if b / m >= a:
    print(n * a)
else:
    res = 0
    mod = n % m
    res += b * (n // m)
    # print()
    if mod * a < b:
        res += mod * a
    else:
        res += b
    print(res)
