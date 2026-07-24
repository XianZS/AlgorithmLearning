import bisect

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
t = int(input())
res = []


def main():
    number = int(input())
    index = bisect.bisect_right(nums, number)
    res.append(str(index))


for _ in range(t):
    main()

print("\n".join(res))
