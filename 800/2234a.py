t = int(input())


for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    judge = True
    for i in range(n - 2):
        if nums[i + 2] != (nums[i] % nums[i + 1]):
            judge = False
    if judge:
        print(f"{nums[0]} {nums[1]}")
    else:
        print("-1")
