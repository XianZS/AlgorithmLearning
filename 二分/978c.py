def main():
    n, m = map(int, input().split())
    ns = list(map(int, input().split()))
    ms = list(map(int, input().split()))
    pred = [0 for _ in range(n)]
    pred[0] = ns[0]
    for index in range(1, n):
        pred[index] += pred[index - 1] + ns[index]
    for cho in ms:
        l, r = 0, n - 1
        index = -1
        while l <= r:
            mid = (l + r) // 2
            if cho < pred[mid]:
                r = mid - 1
            elif cho > pred[mid]:
                l = mid + 1
            elif cho == pred[mid]:
                index = mid
                break
        if index == -1:
            index = l
        if index == 0:
            print(1, cho)
        else:
            print(index + 1, cho - pred[index - 1])


main()
