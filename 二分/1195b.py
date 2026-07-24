import math

n, k = map(int, input().split())
res = 0
# 操作1：a
# 操作2：b
# a+b=n
# 1+2+3+...+b-a=k
# b(1+b)/2-a=k
b = (-3 + math.sqrt(9 + 8 * (n + k))) // 2
# print(b)
print(int(n - b))
