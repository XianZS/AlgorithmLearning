a, b, c = map(int, input().split())

a_c = (a * c) / b
if int(a_c) != a_c:
    a_c = int(a_c) + 1
else:
    a_c = int(a_c)
print(a_c - c)
