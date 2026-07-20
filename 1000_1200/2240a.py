c = int(input())


def main():
    max_number, count = map(int, input().split())
    # nums[i]=c：表示[max_number-count*2^0-count*2^1-count*2^2-count*2^(i-1)]/[2^i]
    # nums = [0 for _ in range(100)]
    i = 0
    res = 0
    dnums = [2**i for i in range(0, 21)]
    while True:
        nl = count * dnums[i]
        if nl < max_number:
            res += count
            max_number -= nl
        elif nl == max_number:
            res += count
            break
        else:
            res += max_number // dnums[i]
            break
        i += 1
    print(res)
    return 0


for _ in range(c):
    main()
