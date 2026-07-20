# 最大公约数（最小公倍数（a,b,c））=最大公约数（a,c）
from math import lcm, gcd

c = int(input())


def main():
    print(">>>")
    res = 0
    n = int(input())
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                if gcd(lcm(x, y), lcm(y, z)) == gcd(x, z):
                    print(x, y, z)
                    res += 1
    print(res)


for _ in range(c):
    main()
