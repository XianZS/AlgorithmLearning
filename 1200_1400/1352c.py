t = int(input())


def main():
    n, k = map(int, input().split())
    mod = k % (n - 1)
    xxx = k // (n - 1)
    res = n * xxx + mod
    if mod == 0:
        res -= 1
    print(res)


for _ in range(t):
    main()
