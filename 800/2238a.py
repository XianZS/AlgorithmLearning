c = int(input())


def main():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum(a) < sum(b):
        print(-1)
        return
    judge = False
    for index in range(n):
        if a[index] < b[index]:
            judge = True
            break
    a.sort()
    b.sort()
    res = 0
    for index in range(n):
        if a[index] < b[index]:
            print(-1)
            return
        else:
            res += abs(a[index] - b[index])
    if judge:
        print(res + c)
    else:
        print(res)


for _ in range(c):
    main()
