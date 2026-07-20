c = int(input())


def main():
    x, y = map(int, input().split())
    if x % y == 0:
        print("yes")
    else:
        print("no")


for _ in range(c):
    main()
