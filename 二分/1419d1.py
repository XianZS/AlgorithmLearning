from re import L


def main():
    res = []
    n = int(input())
    nums = list(map(int, input().split()))
    # print(nums)
    if n < 3:
        print(0)
        for cho in nums:
            print(f"{cho} ", end="")
        return
    nums.sort(reverse=True)
    if n & 1:
        mins, maxs = nums[: (n // 2) + 1], nums[(n // 2) + 1 :]
    else:
        mins, maxs = nums[: n // 2], nums[n // 2 :]
    # print(mins, maxs)
    while mins or maxs:
        if mins:
            p = mins.pop()
            res.append(str(p))
        if maxs:
            p = maxs.pop()
            res.append(str(p))
    if n & 1:
        print(n // 2)
    else:
        print(n // 2 - 1)
    # print(n // 2)
    print(" ".join(res))


main()
