from collections import Counter

t = int(input())


def main():
    n, k = map(int, input().split())
    ks = list(map(int, input().split()))
    # ks.sort(reverse=True)
    cnums = Counter(ks)
    xxx = sorted(set(ks), reverse=True)
    L = len(xxx)
    # need[位置,时间,个数]
    need = [(xxx[index], n - xxx[index], cnums[xxx[index]]) for index in range(L)]
    # print(need)
    index = 0
    live = 0
    for x in range(L):
        node = need[x]
        # print(node)
        for _ in range(node[2]):
            if index < node[0]:
                live += 1
                index += node[1]
            elif index >= node[0]:
                break
    print(live)

    # print("-" * 10)


for _ in range(t):
    main()
