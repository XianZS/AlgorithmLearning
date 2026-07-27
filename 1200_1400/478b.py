def main():
    import bisect

    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    ms = list(map(int, input().split()))
    preds = [0 for _ in range(n)]
    preds[0] = nums[0]
    for index in range(1, n):
        preds[index] = preds[index - 1] + nums[index]
    # print(preds)
    for cho in ms:
        index = bisect.bisect_left(preds, cho)
        # if preds[index - 1] == cho:
        #     index -= 1
        print(index + 1)


main()
