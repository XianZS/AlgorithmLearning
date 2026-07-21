t = int(input())


def main():
    n, m = map(int, input().split())
    s = list(input())
    qs = list(map(int, input().split()))
    B = s.count("B")
    if B == 0:
        for q in qs:
            print(q)
        return
    for q in qs:
        index = 0
        step = 0
        while q:
            if s[index] == "A":
                q -= 1
            if s[index] == "B":
                q = q // 2
            step += 1
            index = (index + 1) % n
        print(step)


for _ in range(t):
    main()
