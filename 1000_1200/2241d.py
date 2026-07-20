c = int(input())


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 选定区间，给区间之内的数字按照【+1,-1,+1,-1,...】的形式进行操作
    c = [0 for _ in range(n)]
    for index in range(n):
        c[index] = a[index] - b[index]
    print(c)


for _ in range(c):
    if main():
        print("YES")
    else:
        print("NO")
