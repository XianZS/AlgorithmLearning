t = int(input())
res = []
for _ in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input()))
    # print(nums)
    for x in range(n - m):
        if nums[x] == 1:
            nums[x] = 0
            nums[x + m] = abs(nums[x + m] - 1)
        else:
            pass
    if sum(nums):
        res.append("no")
    else:
        res.append("yes")


print("\n".join(res))
