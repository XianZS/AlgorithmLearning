nums = list(map(int, input()))

L = len(nums)

for index in range(L):
    if index == 0:
        if nums[index] == 9:
            pass
        else:
            nums[index] = min(abs(9 - nums[index]), nums[index])
    else:
        nums[index] = min(abs(9 - nums[index]), nums[index])
print("".join(str(cho) for cho in nums))
