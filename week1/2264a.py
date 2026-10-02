c = int(input())


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    if n < max(nums):
        print("no")
        return
    sets = list(set(nums))
    if len(sets) != n:
        print("no")
        return
    res = []
    for x in range(n):
        if x + 1 == nums[x]:
            pass
        else:
            res.append(nums[x])
    if not res:
        print("yes")
        return
    j = True
    for index, child in enumerate(res):
        if index == 0:
            continue
        if res[index - 1] < child:
            j = False
            break
    if j:
        print("yes")
    else:
        print("no")


for _ in range(c):
    main()
