# https://codeforces.com/problemset/problem/2242/B

c = int(input())
for x in range(c):
    n = int(input())
    nums = list(map(int, input().split()))
    judge = False
    pred1 = [0 for _ in range(n)]
    pred2 = [0 for _ in range(n)]
    pred3 = [0 for _ in range(n)]
    for index in range(n):
        if index == 0:
            pass
        else:
            pred1[index] += pred1[index - 1]
            pred2[index] += pred2[index - 1]
            pred3[index] += pred3[index - 1]
        if nums[index] == 1:
            pred1[index] += 1
        elif nums[index] == 2:
            pred2[index] += 1
        else:
            pred3[index] += 1
    for a in range(n):
        if pred1[a] >= pred2[a] + pred3[a]:
            for b in range(a + 1, n - 1):
                if (pred1[b] - pred1[a] + pred2[b] - pred2[a]) >= (pred3[b] - pred3[a]):
                    judge = True
                    break
        if judge:
            break

    if judge:
        print("Yes")
    else:
        print("No")
