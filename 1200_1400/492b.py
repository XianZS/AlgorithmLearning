n, l = map(int, input().split())
nums = sorted(set(map(int, input().split())))
# print(nums)
newn = len(nums)
res = []


if newn == 1:
    res.append(abs(0 - nums[0]))
    res.append(abs(nums[0] - l))
else:
    if nums[0] == 0:
        res.append(0)
    else:
        res.append(abs(nums[0] - 0))
    index = 1
    while True:
        res.append(abs(nums[index] - nums[index - 1]) / 2)
        index += 1
        if index == newn:
            break
    if nums[-1] == l:
        res.append(0)
    else:
        res.append(abs(nums[-1] - l))


res.sort(reverse=True)
print(res[0])
