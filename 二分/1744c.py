t = int(input())

ans = []


def main():
    n, c = input().split()
    n = int(n)
    some = input()
    # some = some + some
    if c == "g":
        ans.append(str(0))
        return
    res = -1
    gs = []
    for x in range(2 * n):
        if some[x % n] == "g":
            gs.append(x)
    pg = 0
    L_gs = len(gs)
    for x in range(2 * n):
        if some[x % n] == c:
            while x > gs[pg]:
                # if x > gs[pg]:
                pg += 1
                if pg >= L_gs:
                    break
            if pg >= L_gs:
                break
            res = max(res, gs[pg] - x)
    # print(res)
    ans.append(str(res))


for _ in range(t):
    main()

print("\n".join(ans))
