t = int(input())


def main():
    n, k = map(int, input().split())
    if n == k or k == 1:
        print(1)
        return
    if n > k:
        mod = n % k
        if mod:
            add = k - mod
            temp = (n + add) / n
        else:
            print(1)
            return
        if int(temp) != temp:
            print(int(temp) + 1)
        else:
            print(int(temp))
    if n < k:
        res = k / n
        if int(res) != res:
            print(int(res) + 1)
        else:
            print(int(res))


for _ in range(t):
    main()
