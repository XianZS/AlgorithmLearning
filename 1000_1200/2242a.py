c = int(input())
for _ in range(c):
    n = int(input())
    nums = list(map(int, input().split()))
    if max(nums) >= 3:
        print("yes")
    elif nums.count(2) >= 2:
        print("yes")
    else:
        print("no")
