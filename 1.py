a = 1
b = 4
c = -5
print('{a}'.format(a,b,c))


def disk(a, b, c):
    return b**2 - 4 * a * c


def problem(a, b, kd):
    return (-b + kd) / (2 * a)


d = disk(a, b, c)
if d < 0:
    print("Wrong input")
elif d == 0:
    print("x1 =", problem(a, b, 0))
else:
    print("x1 =", problem(a, b, -d**0.5))
    print("x2 =", problem(a, b, d**0.5))
