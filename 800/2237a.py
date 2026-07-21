c = int(input())
result = []
for _ in range(c):
    n = int(input())
    nums = list(map(int, input().split()))
    res = nums.copy()
    dnums = [1 for _ in range(n)]
    news = sorted(nums)
    for cho in news:
        index = nums.index(cho)
        dnums[index] = 0
        judge = True
        for x in range(index + 1, n):
            if dnums[x]:
                dnums[x] = 0
                res[x] = cho
                judge = False
        # if judge:
        #     break
    result.append(str(sum(res)))
    # print(res)
print("\n".join(result))
