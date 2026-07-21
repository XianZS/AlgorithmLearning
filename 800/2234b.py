t = int(input())


for _ in range(t):
    n = int(input())
    # n=a+b=a+12*k
    if n == 10:
        print(-1)
    elif n % 12 != 10:
        print(n % 12, n - n % 12)
    else:
        print(22, n - 22)
