t = int(input())
res = []
for _ in range(t):
    n, x, y, z = map(int, input().split())
    time1 = n / (x + y)
    time2 = 0
    if n / x < z:
        time2 = n / x
    else:
        time2 = z + (n - x * z) / (x + 10 * y)
    time = min(time1, time2)
    if int(time) != time:
        res.append(str(int(time) + 1))
    else:
        res.append(str(int(time)))

print("\n".join(res))
