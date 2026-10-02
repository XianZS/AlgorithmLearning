c = int(input())


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    dnums = {}
    for index, number in enumerate(nums):
        if number in dnums:
            dnums[number] += 1
        else:
            dnums[number] = 1
    if 0 not in dnums:
        print(-1)
        return
    if dnums[0] < 2:
        print(-1)
        return
    if nums[0] == 0 and nums[-1] == 0:
        print(0)
        return
    if nums[0] + nums[-1] == 1:
        print(1)
        return
    if nums[0] + nums[-1] == 2:
        print(2)
        return


for _ in range(c):
    main()
