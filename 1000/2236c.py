import math

t = int(input())
res = []

for _ in range(t):
    a, b, x = map(int, input().split())
    k, ans = 0, math.inf
    while a != b:
        a, b = max(a, b), min(a, b)
        ans = min(ans, abs(a - b) + k)
        a = a // x
        k += 1
    ans = min(ans, k)
    res.append(str(ans))


print("\n".join(res))
