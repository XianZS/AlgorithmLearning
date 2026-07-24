t = int(input())

xxx = []


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    some = [[0 for _ in range(n)] for _ in range(n)]
    res = 0
    for x in range(n):
        for y in range(x + 1, n):
            # some[x][y] = nums[y] - nums[x]
            if nums[y] - nums[x] == y - x:
                # print(f"({x},{y})")
                res += 1
    # print()
    xxx.append(str(res))


for _ in range(t):
    main()

print("\n".join(xxx))
