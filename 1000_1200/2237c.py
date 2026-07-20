c = int(input())

res = []


def make(nums, x):
    nums[x], nums[x + 1] = nums[x + 1], nums[x] + nums[x + 1]


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    for x in range(n - 1):
        if nums[x] > nums[x + 1]:
            make(nums, x)
    # print(max(nums))
    res.append(str(max(nums)))


for _ in range(c):
    main()
print("\n".join(res))
