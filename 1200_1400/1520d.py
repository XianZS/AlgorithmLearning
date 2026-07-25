from collections import defaultdict

t = int(input())

xxx = []


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    res = defaultdict(int)
    for index in range(n):
        res[nums[index] - index] += 1
    # print(res)
    xx = res.values()
    some = 0
    for cho in xx:
        if cho > 1:
            cho -= 1
            some += cho * (cho + 1) // 2
        else:
            pass
    xxx.append(str(some))


for _ in range(t):
    main()

print("\n".join(xxx))
