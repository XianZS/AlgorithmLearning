def main():
    n, d = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    res = 0
    index = 0
    people = n
    d += 1
    while True:
        x = d / nums[index]
        if int(x) == x:
            need = int(x)
        else:
            need = int(x) + 1
        if need == people:
            res += 1
            print(res)
            break
        elif need < people:
            people -= need
            res += 1
            index += 1
        else:
            print(res)
            break


main()
