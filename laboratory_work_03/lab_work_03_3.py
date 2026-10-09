from math import isfinite

xb = float(input("Введите Xнач: "))
xe = float(input("Введите Xкон: "))
dx = float(input("Введите шаг dx: "))
eps = float(input("Введите точность epsilon: "))

if not all(isfinite(v) for v in (xb, xe, dx, eps)) or xb > xe or dx <= 0 or eps <= 0:
    print("Нужно Xнач <= Xкон, dx > 0, epsilon > 0; числа должны быть конечными.")
elif not (xe < -1 or xb > 1):
    print("Весь отрезок должен находиться в области X < -1 или X > 1.")
else:
    print("ln((X + 1) / (X - 1)), вариант 1")
    print("Xнач = {}, Xкон = {}, dx = {}, epsilon = {}".format(xb, xe, dx, eps))
    print("+------------+----------------+---------+")
    print("|     X      |       Y        | Членов  |")
    print("+------------+----------------+---------+")
    i = 0
    x = xb
    while x <= xe or abs(x - xe) <= dx * 1e-9:
        if x > xe:
            x = xe
        term = 2 / x
        y = term
        n = 1
        q = (1 / x) ** 2
        next_term = term * q * (2 * n - 1) / (2 * n + 1)
        while abs(next_term) / (1 - q) > eps:
            y += next_term
            term = next_term
            n += 1
            next_term = term * q * (2 * n - 1) / (2 * n + 1)
        print("|{:12.4f}|{:16.10f}|{:9}|".format(x, y, n))
        i += 1
        x = xb + i * dx
    print("+------------+----------------+---------+")
